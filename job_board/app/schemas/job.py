from pydantic import BaseModel, ConfigDict
from app.schemas.company import CompanyRead
from app.schemas.skill import SkillRead


class JobCreate(BaseModel):
    title: str
    description: str
    location: str
    min_salary: int
    max_salary: int
    company_id: int

class JobRead(BaseModel):
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
    model_config = ConfigDict(from_attributes=True)

    title: str
    description: str
    location: str
    min_salary: int
    max_salar: int
    company: CompanyRead
    skills: list[SkillRead] = []