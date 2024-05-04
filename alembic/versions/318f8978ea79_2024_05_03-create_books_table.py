"""create books table

Revision ID: 318f8978ea79
Revises: 
Create Date: 2024-05-03 23:04:21.420397

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "318f8978ea79"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "books",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("author", sa.String(255), nullable=False),
        sa.Column("year", sa.Integer, nullable=False),
        sa.Column("isbn", sa.String(13), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("books")
