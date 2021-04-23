"""empty message

Revision ID: 9ee126748d86
Revises: 9d2df03b1d09
Create Date: 2021-04-22 23:05:13.783561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ee126748d86'
down_revision = '9d2df03b1d09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'cliente', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cliente', type_='unique')
    # ### end Alembic commands ###