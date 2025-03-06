"""Add nb assets ready column

Revision ID: a66508788c53
Revises: 1e150c2cea4d
Create Date: 2021-11-23 00:07:43.717653

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a66508788c53"
down_revision = "1e150c2cea4d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "task", sa.Column("nb_assets_ready", sa.Integer(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("task", "nb_assets_ready")
    # ### end Alembic commands ###
