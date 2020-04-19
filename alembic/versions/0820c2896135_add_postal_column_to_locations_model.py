"""Add postal column to locations model

Revision ID: 0820c2896135
Revises: 
Create Date: 2020-04-19 20:42:42.403622

"""
from typing import Optional
from alembic import op
import sqlalchemy as sa


revision: str = '0820c2896135'
down_revision: Optional[str] = None
branch_labels: Optional[str] = None
depends_on: Optional[str] = None


def upgrade() -> None:
    """Upgrades migration."""
    op.add_column('location', sa.Column('postal', sa.String(), nullable=True))
    op.create_index(op.f('ix_location_postal'), 'location', ['postal'], unique=False)


def downgrade() -> None:
    """Downgrades migration."""
    op.drop_index(op.f('ix_location_postal'), table_name='location')
    op.drop_column('location', 'postal')
