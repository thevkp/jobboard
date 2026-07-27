from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app.core.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.company import Company
    from app.models.skill import Skill
    from app.models.application import Application
    from app.models.user import User

class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(90))
    location: Mapped[str]= mapped_column(String(50))
    min_salary: Mapped[int]
    max_salary: Mapped[int]


    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"))

    company: Mapped["Company"] = relationship(back_populates="jobs")

    skills: Mapped[list["Skill"]] = relationship(
        secondary="job_skills", back_populates="jobs"
    )

    applications: Mapped[list["Application"]] = relationship(
        back_populates="job"
    )

    saved_by_users: Mapped[list["User"]] = relationship(
        secondary="saved_jobs", back_populates="saved_jobs"
    )