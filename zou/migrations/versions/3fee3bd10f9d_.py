"""empty message

Revision ID: 3fee3bd10f9d
Revises: 45c2de366e66
Create Date: 2018-10-23 16:46:02.990772

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "3fee3bd10f9d"
down_revision = "45c2de366e66"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "output_file",
        sa.Column(
            "data", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
    )
    op.add_column(
        "working_file",
        sa.Column(
            "data", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("working_file", "data")
    op.drop_column("output_file", "data")
    # ### end Alembic commands ###
