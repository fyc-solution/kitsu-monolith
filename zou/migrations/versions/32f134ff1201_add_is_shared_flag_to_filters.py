"""add is_shared flag to filters

Revision ID: 32f134ff1201
Revises: 57222395f2be
Create Date: 2024-05-17 00:50:00.493167

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "32f134ff1201"
down_revision = "57222395f2be"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("search_filter", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("is_shared", sa.Boolean(), nullable=True)
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("search_filter", schema=None) as batch_op:
        batch_op.drop_column("is_shared")
