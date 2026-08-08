from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.application import Application
    from app.models.job import Job
    from app.models.company import Company

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    company_id: Mapped[int | None] = mapped_column(ForeignKey("companies.id"))

    company: Mapped["Company | None"] = relationship(back_populates="employees")

    applications: Mapped[list["Application"]] = relationship(back_populates="user")
    saved_jobs: Mapped[list["Job"]] = relationship(
        secondary="saved_jobs", back_populates="saved_by_users")