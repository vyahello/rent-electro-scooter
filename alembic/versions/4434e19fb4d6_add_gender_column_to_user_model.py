"""Add 'gender' column to user model

Revision ID: 4434e19fb4d6
Revises: 0820c2896135
Create Date: 2020-04-19 20:43:20.702240

"""
from typing import Optional
from alembic import op
import sqlalchemy as sa

revision: str = '4434e19fb4d6'
down_revision: str = '0820c2896135'
branch_labels: Optional[str] = None
depends_on: Optional[str] = None


def upgrade() -> None:
    """Upgrades migration."""
    op.add_column('users', sa.Column('gender', sa.String(), nullable=True))


def downgrade() -> None:
    """Downgrades migration."""
    op.drop_column('users', 'gender')
