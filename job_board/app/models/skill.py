from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import TYPE_CHECKING
from app.core.database import Base


if TYPE_CHECKING:
    from app.models.job import Job




class Skill(Base):
    __tablename__ = "skills"


    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)

    jobs: Mapped[list["Job"]] = relationship(
        secondary="job_skills", back_populates="skills"
    )