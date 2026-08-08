from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.core.database import Base
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.job import Job
    from app.models.user import User


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str | None]
    website: Mapped[str | None]
    location: Mapped[str] = mapped_column(String(70))

    employees: Mapped[list["User"]] = relationship(back_populates="company")

    jobs: Mapped[list["Job"]] = relationship(back_populates="company")