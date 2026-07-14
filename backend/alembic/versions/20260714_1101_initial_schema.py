"""initial schema

Revision ID: 20260714_1101
Revises:
Create Date: 2026-07-14 11:01:00
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "20260714_1101"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=64), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("avatar", sa.String(length=512), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_id"), "user", ["id"], unique=False)
    op.create_index(op.f("ix_user_username"), "user", ["username"], unique=True)

    op.create_table(
        "resume",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("filename", sa.String(length=255), nullable=False),
        sa.Column("filepath", sa.String(length=1024), nullable=False),
        sa.Column("analysis_score", sa.Float(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_resume_id"), "resume", ["id"], unique=False)
    op.create_index(op.f("ix_resume_user_id"), "resume", ["user_id"], unique=False)

    op.create_table(
        "job_record",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("job_name", sa.String(length=255), nullable=False),
        sa.Column("jd_content", sa.Text(), nullable=False),
        sa.Column("match_score", sa.Float(), nullable=True),
        sa.Column("result", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_job_record_id"), "job_record", ["id"], unique=False)
    op.create_index(op.f("ix_job_record_user_id"), "job_record", ["user_id"], unique=False)

    op.create_table(
        "interview",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("job_name", sa.String(length=255), nullable=False),
        sa.Column("summary", sa.Text(), nullable=True),
        sa.Column("score", sa.Float(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_interview_id"), "interview", ["id"], unique=False)
    op.create_index(op.f("ix_interview_user_id"), "interview", ["user_id"], unique=False)

    op.create_table(
        "chat_history",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("session_id", sa.String(length=64), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("role", sa.String(length=32), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_chat_history_id"), "chat_history", ["id"], unique=False)
    op.create_index(op.f("ix_chat_history_session_id"), "chat_history", ["session_id"], unique=False)
    op.create_index(op.f("ix_chat_history_user_id"), "chat_history", ["user_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_chat_history_user_id"), table_name="chat_history")
    op.drop_index(op.f("ix_chat_history_session_id"), table_name="chat_history")
    op.drop_index(op.f("ix_chat_history_id"), table_name="chat_history")
    op.drop_table("chat_history")

    op.drop_index(op.f("ix_interview_user_id"), table_name="interview")
    op.drop_index(op.f("ix_interview_id"), table_name="interview")
    op.drop_table("interview")

    op.drop_index(op.f("ix_job_record_user_id"), table_name="job_record")
    op.drop_index(op.f("ix_job_record_id"), table_name="job_record")
    op.drop_table("job_record")

    op.drop_index(op.f("ix_resume_user_id"), table_name="resume")
    op.drop_index(op.f("ix_resume_id"), table_name="resume")
    op.drop_table("resume")

    op.drop_index(op.f("ix_user_username"), table_name="user")
    op.drop_index(op.f("ix_user_id"), table_name="user")
    op.drop_table("user")
