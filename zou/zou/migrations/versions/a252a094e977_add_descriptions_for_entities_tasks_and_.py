"""Add descriptions for entities tasks and statuses

Revision ID: a252a094e977
Revises: 1bb55759146f
Create Date: 2024-06-20 20:37:21.885953

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a252a094e977"
down_revision = "1bb55759146f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "task_type", sa.Column("description", sa.Text(), nullable=True)
    )
    op.add_column(
        "task_status", sa.Column("description", sa.Text(), nullable=True)
    )
    op.add_column(
        "entity_type", sa.Column("description", sa.Text(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("task_type", "description")
    op.drop_column("task_status", "description")
    op.drop_column("entity_type", "description")

    # ### end Alembic commands ###
