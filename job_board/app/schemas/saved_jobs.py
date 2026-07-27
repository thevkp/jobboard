from pydantic import BaseModel

class SavedJobCreate(BaseModel):
    job_id: int
    user_id: int
    