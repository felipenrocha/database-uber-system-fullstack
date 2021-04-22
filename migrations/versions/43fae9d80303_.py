"""empty message

Revision ID: 43fae9d80303
Revises: dbb8ece4c093
Create Date: 2021-04-21 21:37:39.702538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43fae9d80303'
down_revision = 'dbb8ece4c093'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('modelo', sa.String(), nullable=True),
    sa.Column('chassi', sa.String(), nullable=True),
    sa.Column('marca', sa.String(), nullable=True),
    sa.Column('ano', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('carro')
    # ### end Alembic commands ###