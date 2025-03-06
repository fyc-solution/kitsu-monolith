"""Add build job model

Revision ID: 54ee0d1d60ba
Revises: 523ee9647bee
Create Date: 2019-06-06 14:13:55.135620

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision = "54ee0d1d60ba"
down_revision = "523ee9647bee"
branch_labels = None
depends_on = None


STATUSES = [
    ("running", "Running"),
    ("failed", "Failed"),
    ("suceeded", "Succeeded"),
]

TYPES = [
    ("archive", "Archive"),
    ("movie", "Movie"),
]


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "build_job",
        sa.Column(
            "id",
            sqlalchemy_utils.types.uuid.UUIDType(binary=False),
            default=uuid.uuid4,
            nullable=False,
        ),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column(
            "status",
            sqlalchemy_utils.types.choice.ChoiceType(STATUSES),
            nullable=True,
        ),
        sa.Column(
            "job_type",
            sqlalchemy_utils.types.choice.ChoiceType(TYPES),
            nullable=True,
        ),
        sa.Column("ended_at", sa.DateTime(), nullable=True),
        sa.Column(
            "playlist_id",
            sqlalchemy_utils.types.uuid.UUIDType(binary=False),
            default=uuid.uuid4,
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["playlist_id"],
            ["playlist.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_build_job_playlist_id"), table_name="build_job")
    op.drop_table("build_job")
    # ### end Alembic commands ###
