from pydantic import BaseModel, ConfigDict
from app.schemas.company import CompanyRead
from app.schemas.skill import SkillRead


class JobCreate(BaseModel):
    # what a client sends to CREATE a job
    title: str
    description: str
    location: str
    min_salary: int
    max_salary: int
    # company_id: int # this should not 

class JobRead(BaseModel):
    # what the SERVER sends BACK to the client
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    location: str
    min_salary: int
    max_salary: int
    company: CompanyRead
    skills: list[SkillRead] = []

class JobUpdate(BaseModel):
    # what a client sends to UPDATE a job - all optional
    model_config = ConfigDict(from_attributes=True)

    title: str | None = None
    description: str | None = None
    location: str | None = None
    min_salary: int | None = None
    max_salary: int | None = None
    # company: CompanyRead 
    skills: list[SkillRead] = []