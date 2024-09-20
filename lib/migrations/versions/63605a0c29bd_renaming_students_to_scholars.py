"""Renaming students to scholars

Revision ID: 63605a0c29bd
Revises: 791279dd0760
Create Date: 2024-09-20 11:52:35.750505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63605a0c29bd'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
