# Projeto final de Banco de Dados: SGBD para Serviços Eletrônicos na Área do Transporte Privado Urbano com Python Flask

Modelo Entidade Relacional: 

![Alt-Text](mer.png)


Modelo Relacional do Banco de Dados:

![Alt-Text](ModeloRELACIONAL.png)

# Instalation Process

## Pré-requisitos


## Por onde eu começo?

Existem algumas formas de você configurar o seu ambiente. Nesta seção iremos apresentar apenas uma das formas possíveis.

* 1. O primeiro passo é fazer o checkout do seu código. Utilizando um terminal, faça um clone do repositório.

```
git clone https://gitlab.com/felipenrocha19/banco-de-dados-tf.git
```
* 2. Criação de um ambiente virtual:

```
python3 -m venv banco-de-dados-tf/env
```

* 3. Entre no repositório

```
cd banco-de-dados-tf
```

* 4. O próximo passo é ativar o terminal e carregar as configurações python.

```
source env/bin/activate
```

* 5. Agora você precisa instalar as bibliotecas utilizadas pela ferramenta Flask e SQLAlchemy.
```
pip3 install -r requirements.txt
```

* 6. Criando o Banco de Dados: (Estou utilizando o nome de uber_db p/ facilitar no desenvolvimento)

É necessário o Sistema PostgreSQL e que já possua um usuário:

P/ Linux:
```
sudo -u name_of_user createdb uber_db
```
P/ checar o banco de dados pelo terminal:
```

psql -U name_of_user -d uber_db
```


* 7. O último passo é exportar as váriaveis de ambiente necessárias p/ o deploy. Como esse é um trabalho de cunho puramente educativo, estou setando sempre para modo de desenvolvimento:

Comando no Linux:

```
export APP_SETTINGS="config.DevelopmentConfig"

export DATABASE_URL="postgresql:///uber_db"
```

Comando no Windows:

```
set APP_SETTINGS="config.DevelopmentConfig"

set DATABASE_URL="postgresql:///uber_db"
```


Pronto! Para testar o código, basta executar:

Inicializando o Banco de dados e criando as tabelas:
```
python manage.py db init
python manage.py db migrate
python manager.py db upgrade
```

```
python manage.py runserver

```
Acesse em: http://127.0.0.1:5000/


* Comandos adicionais:

Migrate:
```
python manage.py db init
python manage.py db migrate
python manager.py db upgrade

```

Seed (Tabelas: Tipo Uber, Métodos Pagamento, Estados da Viagem, Pessoas):

```
python tipos_uber_seed.py
python metodos_pagamento_seed.py
python estados_seed.py
python pessoas_seed.py


```



