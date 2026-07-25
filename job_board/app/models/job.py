from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app.core.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.company import Company
    from app.models.skill import Skill

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