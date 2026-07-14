from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin


class User(TimestampMixin, Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    avatar: Mapped[str | None] = mapped_column(String(512), nullable=True)

    resumes: Mapped[list["Resume"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    job_records: Mapped[list["JobRecord"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    interviews: Mapped[list["Interview"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    chat_histories: Mapped[list["ChatHistory"]] = relationship(back_populates="user", cascade="all, delete-orphan")
