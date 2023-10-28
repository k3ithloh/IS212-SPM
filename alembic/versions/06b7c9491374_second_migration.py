"""second migration

Revision ID: 06b7c9491374
Revises: 30efb1b315e3
Create Date: 2023-10-15 13:21:25.796231

"""
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import mysql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "06b7c9491374"
down_revision: Union[str, None] = "30efb1b315e3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "CLERK_STAFF_MATCH",
        "clerk_id",
        existing_type=mysql.INTEGER(),
        type_=sa.String(length=155),
        existing_nullable=False,
    )
    op.alter_column(
        "ROLE_DETAILS",
        "role_description",
        existing_type=mysql.MEDIUMTEXT(),
        type_=sa.String(length=50000),
        existing_nullable=True,
    )
    op.alter_column(
        "ROLE_LISTINGS",
        "role_listing_desc",
        existing_type=mysql.MEDIUMTEXT(),
        type_=sa.String(length=50000),
        existing_nullable=True,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "ROLE_LISTINGS",
        "role_listing_desc",
        existing_type=sa.String(length=50000),
        type_=mysql.MEDIUMTEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "ROLE_DETAILS",
        "role_description",
        existing_type=sa.String(length=50000),
        type_=mysql.MEDIUMTEXT(),
        existing_nullable=True,
    )
    op.alter_column(
        "CLERK_STAFF_MATCH",
        "clerk_id",
        existing_type=sa.String(length=155),
        type_=mysql.INTEGER(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
