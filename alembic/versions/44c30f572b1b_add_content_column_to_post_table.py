"""add content column to post table

Revision ID: 44c30f572b1b
Revises: 2bfb4bbf7f08
Create Date: 2024-04-14 10:59:30.570162

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44c30f572b1b'
down_revision: Union[str, None] = '2bfb4bbf7f08'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
