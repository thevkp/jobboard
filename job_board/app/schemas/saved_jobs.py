from pydantic import BaseModel
from app.schemas.job import JobRead

class SavedJobCreate(BaseModel):
    job_id: int
    user_id: int

class SavedJobRead(BaseModel):
    job: JobRead
    job_id: int