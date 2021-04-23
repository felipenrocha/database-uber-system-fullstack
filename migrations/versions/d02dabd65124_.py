"""empty message

Revision ID: d02dabd65124
Revises: 83a2c374aa59
Create Date: 2021-04-22 23:15:34.498058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd02dabd65124'
down_revision = '83a2c374aa59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'posicao', ['id'])
    op.add_column('viagem', sa.Column('destino_id', sa.Integer(), nullable=False))
    op.add_column('viagem', sa.Column('origem_id', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'viagem', ['id'])
    op.create_foreign_key(None, 'viagem', 'posicao', ['origem_id'], ['id'])
    op.create_foreign_key(None, 'viagem', 'posicao', ['destino_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'viagem', type_='foreignkey')
    op.drop_constraint(None, 'viagem', type_='foreignkey')
    op.drop_constraint(None, 'viagem', type_='unique')
    op.drop_column('viagem', 'origem_id')
    op.drop_column('viagem', 'destino_id')
    op.drop_constraint(None, 'posicao', type_='unique')
    # ### end Alembic commands ###