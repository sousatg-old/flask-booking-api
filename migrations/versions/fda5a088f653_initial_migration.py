"""Initial migration

Revision ID: fda5a088f653
Revises: 
Create Date: 2020-08-30 11:07:56.158589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fda5a088f653'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('booking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.String(length=200), nullable=True),
    sa.Column('end_time', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('booking')
    # ### end Alembic commands ###
