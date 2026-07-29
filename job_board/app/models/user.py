from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.application import Application
    from app.models.job import Job

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(255), unique=True)

    applications: Mapped[list["Application"]] = relationship(back_populates="user")
    saved_jobs: Mapped[list["Job"]] = relationship(
        secondary="saved_jobs", back_populates="saved_by_users")