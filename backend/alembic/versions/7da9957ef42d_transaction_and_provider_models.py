"""transaction and provider models

Revision ID: 7da9957ef42d
Revises: 3e285df335d0
Create Date: 2021-06-20 09:25:47.663284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7da9957ef42d'
down_revision = '3e285df335d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('provider',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('balance', sa.Float(), server_default='0', nullable=False),
    sa.Column('payment_amount', sa.Float(), server_default='0', nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_provider_id'), 'provider', ['id'], unique=False)
    op.create_index(op.f('ix_provider_name'), 'provider', ['name'], unique=False)
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('provider_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['provider_id'], ['provider.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_transaction_id'), 'transaction', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_transaction_id'), table_name='transaction')
    op.drop_table('transaction')
    op.drop_index(op.f('ix_provider_name'), table_name='provider')
    op.drop_index(op.f('ix_provider_id'), table_name='provider')
    op.drop_table('provider')
    # ### end Alembic commands ###
