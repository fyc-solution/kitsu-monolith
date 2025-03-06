"""Remove unique constraint for TaskStatus.is_default

Revision ID: 05ac7e8caa21
Revises: 0cf5e0e035fa
Create Date: 2022-06-16 14:26:54.695564

"""

from alembic import op
from sqlalchemy import orm
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from zou.migrations.utils.base import BaseMixin

# revision identifiers, used by Alembic.
revision = "05ac7e8caa21"
down_revision = "0cf5e0e035fa"
branch_labels = None
depends_on = None


class TaskStatus(declarative_base(), BaseMixin):
    """
    Describe the state of a task. A status marked as reviewable expects a
    preview file linked to relate comment.
    """

    __tablename__ = "task_status"
    name = sa.Column(sa.String(40), nullable=False)
    short_name = sa.Column(
        sa.String(10), unique=True, nullable=False, index=True
    )
    color = sa.Column(sa.String(7), nullable=False)

    is_done = sa.Column(sa.Boolean(), default=False, index=True)
    is_artist_allowed = sa.Column(sa.Boolean(), default=True)
    is_client_allowed = sa.Column(sa.Boolean(), default=True)
    is_retake = sa.Column(sa.Boolean(), default=False)
    is_feedback_request = sa.Column(sa.Boolean(), default=False, index=True)
    is_default = sa.Column(sa.Boolean(), default=False, index=True)
    shotgun_id = sa.Column(sa.Integer)


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_task_status_is_default", table_name="task_status")
    op.create_index(
        op.f("ix_task_status_is_default"),
        "task_status",
        ["is_default"],
        unique=False,
    )
    # ### end Alembic commands ###

    # set all the TaskStatus.is_default == None to False
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    task_statuses = (
        session.query(TaskStatus).filter(TaskStatus.is_default == None).all()
    )
    for task_status in task_statuses:
        task_status.is_default = False

    session.commit()


def downgrade():
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    task_statuses = (
        session.query(TaskStatus).filter(TaskStatus.is_default == False).all()
    )
    for task_status in task_statuses:
        task_status.is_default = None

    session.commit()
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_task_status_is_default"), table_name="task_status")
    op.create_index(
        "ix_task_status_is_default",
        "task_status",
        ["is_default"],
        unique=False,
    )
    # ### end Alembic commands ###
