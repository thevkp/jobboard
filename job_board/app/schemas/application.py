from pydantic import BaseModel
from datetime import datetime
from app.models.application import JobStatus
from app.schemas.user import UserRead
from app.schemas.job import JobRead


class ApplicationCreate(BaseModel):
    user_id: int
    job_id: int



class ApplicationRead(BaseModel):
    id: int
    status: JobStatus
    applied_at: datetime
    user: UserRead
    job: JobRead

class ApplicationUpdate(BaseModel):
    status: JobStatus
    user: UserRead
    job: JobRead