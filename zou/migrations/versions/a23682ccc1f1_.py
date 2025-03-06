"""empty message

Revision ID: a23682ccc1f1
Revises: 9bd17364fc18
Create Date: 2018-04-20 10:39:31.976959

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = "a23682ccc1f1"
down_revision = "9bd17364fc18"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "desktop_login_log",
        sa.Column(
            "id",
            sqlalchemy_utils.types.uuid.UUIDType(binary=False),
            nullable=False,
        ),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column(
            "person_id",
            sqlalchemy_utils.types.uuid.UUIDType(binary=False),
            nullable=False,
        ),
        sa.Column("date", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["person_id"],
            ["person.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_desktop_login_log_person_id"),
        "desktop_login_log",
        ["person_id"],
        unique=False,
    )
    op.add_column(
        "asset_instance", sa.Column("active", sa.Boolean(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("asset_instance", "active")
    op.drop_index(
        op.f("ix_desktop_login_log_person_id"), table_name="desktop_login_log"
    )
    op.drop_table("desktop_login_log")
    # ### end Alembic commands ###
