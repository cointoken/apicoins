"""create tables

Revision ID: 7dc2bb0c7311
Revises: 
Create Date: 2018-08-30 12:00:37.877535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7dc2bb0c7311'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('currency', sa.String(length=20), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('passphrase', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('deposits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deposit_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('currency', sa.String(length=20), nullable=True),
    sa.Column('from_address', sa.String(length=255), nullable=True),
    sa.Column('to_address', sa.String(length=255), nullable=True),
    sa.Column('amount', sa.DECIMAL(precision=16, scale=8), nullable=True),
    sa.Column('fee', sa.DECIMAL(precision=16, scale=8), nullable=True),
    sa.Column('txid', sa.String(length=255), nullable=True),
    sa.Column('status', sa.String(length=1), nullable=True),
    sa.Column('deposit_time', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('deposit_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('deposits')
    op.drop_table('coins')
    # ### end Alembic commands ###