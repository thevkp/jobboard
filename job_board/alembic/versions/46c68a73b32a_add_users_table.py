"""add users table

Revision ID: 46c68a73b32a
Revises: a097359abfa0
Create Date: 2026-08-03 13:40:34.468963

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46c68a73b32a'
down_revision: Union[str, Sequence[str], None] = 'a097359abfa0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    # Step 1: add column as nullable first (existing rows get NULL, which is allowed)
    op.add_column('users', sa.Column('hashed_password', sa.String(), nullable=True))

    # Step 2: backfill existing rows with a placeholder hash
    # (this user won't be able to log in with a real password until they reset it,
    # but the column is no longer NULL)
    op.execute("UPDATE users SET hashed_password = 'INVALID_NEEDS_RESET' WHERE hashed_password IS NULL")

    # Step 3: now that no NULLs remain, enforce NOT NULL
    op.alter_column('users', 'hashed_password', nullable=False)


def downgrade() -> None:
    op.drop_column('users', 'hashed_password')