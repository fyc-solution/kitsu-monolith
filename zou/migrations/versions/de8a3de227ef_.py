"""empty message

Revision ID: de8a3de227ef
Revises: 45c2de366e66
Create Date: 2018-10-22 19:51:59.580865

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision = "de8a3de227ef"
down_revision = "0ef6416a507b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "comment_preview_link",
        sa.Column(
            "comment",
            sqlalchemy_utils.types.uuid.UUIDType(binary=False),
            default=uuid.uuid4,
            nullable=False,
        ),
        sa.Column(
            "preview_file",
            sqlalchemy_utils.types.uuid.UUIDType(binary=False),
            default=uuid.uuid4,
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["comment"],
            ["comment.id"],
        ),
        sa.ForeignKeyConstraint(
            ["preview_file"],
            ["preview_file.id"],
        ),
        sa.PrimaryKeyConstraint("comment", "preview_file"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("comment_preview_link")
    # ### end Alembic commands ###
