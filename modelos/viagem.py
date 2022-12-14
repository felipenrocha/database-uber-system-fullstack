from app import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from modelos.motorista import Motorista
from modelos.cliente import Cliente


class Viagem(db.Model):
    __tablename__ = 'viagem'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    estado_id = db.Column(db.Integer,
                          db.ForeignKey('estado.id'),
                          nullable=False)
    _estado = relationship("Estado", back_populates="relationships")

    motorista_id = db.Column(db.Integer,
                             db.ForeignKey('motorista.id'),
                             nullable=False)  # many to one

    cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)

    _posicao = relationship("Posicao",
                            back_populates="_posicao")  # one to many posicao

    metodo_id = Column(Integer,
                       ForeignKey('metodo_pagamento.id'),
                       nullable=False)

    def __init__(self, valor, estado_id, motorista_id, cliente_id, metodo_id):
        self.valor = valor
        self.estado_id = estado_id
        self.motorista_id = motorista_id
        self.cliente_id = cliente_id
        self.metodo_id = metodo_id

    def serialize(self):
        return {
            'id': self.id,
            'valor': self.valor,
            'estado': Estado.query.get(self.estado_id).serialize(),
            'motorista': Motorista.query.get(self.motorista_id).serialize(),
            'cliente': Cliente.query.get(self.cliente_id).serialize(),
            'posicao_origem': self.getPosicaoOrigem().serialize(),
            'posicao_destino': self.getPosicaoDestino().serialize(),
            'metodo_pagamento': self.getMetodosPagamento()
        }

    def getPosicaoOrigem(self):
        posicao = Posicao.query.filter_by(viagem_id=self.id,
                                          tipo='origem').first()
        return posicao

    def getPosicaoDestino(self):
        posicao = Posicao.query.filter_by(viagem_id=self.id,
                                          tipo='destino').first()
        return posicao

    def getAll():
        return Viagem.query.all()

    def getMetodosPagamento(self):
        metodo = MetodoPagamento.query().get(self.metodo_id)
        return metodo.serialize()


# One (Viagem) to Many (Posicao)


class Posicao(db.Model):
    __tablename__ = 'posicao'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    tipo = db.Column(db.String(10), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    viagem_id = Column(Integer, ForeignKey('viagem.id'))
    _posicao = relationship("Viagem", back_populates="_posicao")

    def __init__(self, tipo, latitude, longitude, viagem_id):
        self.latitude = latitude
        self.longitude = longitude
        self.tipo = tipo
        self.viagem_id = viagem_id

    def serialize(self):
        return {
            'id': self.id,
            'latitude': self.latitude,
            'longitude': self.longitude
        }


class Estado(db.Model):
    __tablename__ = 'estado'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    descricao = Column(db.String(35), nullable=False)

    relationships = relationship("Viagem", back_populates="_estado")

    def __init__(self, descricao):
        self.descricao = descricao

    def getAll():
        estadosQuery = Estado.query.all()
        estados = list()
        for estado in estadosQuery:
            estados.append(estado.serialize())
        return estados

    def serialize(self):
        return {'id': self.id, 'descricao': self.descricao}


class MetodoPagamento(db.Model):
    __tablename__ = 'metodo_pagamento'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    tipo = Column(db.String(35), nullable=False)
   

    def __init__(self, tipo):
        self.tipo = tipo

    def serialize(self):
        return {'id': self.id, 'nome': self.tipo}

    def getAll():
        metodosQuery = MetodoPagamento.query.all()
        metodos = list()
        for metodo in metodosQuery:
            metodos.append(metodo.serialize())
        print(metodos)
        return metodos
