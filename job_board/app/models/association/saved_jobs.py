from app.core.database import Base
# from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Table, Column, Integer


# class SavedJob(Base):
#     __tablename__ = "saved_jobs"

#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id"))

saved_jobs = Table(
    "saved_jobs",
    Base.metadata,
    Column("job_id", Integer, ForeignKey("jobs.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
)