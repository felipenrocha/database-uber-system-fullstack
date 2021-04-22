"""empty message

Revision ID: 9aa9107112c5
Revises: d478eef1d0b4
Create Date: 2021-04-22 15:39:05.529385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9aa9107112c5'
down_revision = 'd478eef1d0b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tipo_uber',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(), nullable=True),
    sa.Column('multiplicador', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tipo_uber')
    # ### end Alembic commands ###