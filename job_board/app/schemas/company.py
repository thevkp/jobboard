from pydantic import BaseModel, ConfigDict


class CompanyCreate(BaseModel):
    title: str
    description: str | None = None
    website: str | None = None
    location: str


class CompanyRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None = None
    website: str | None = None
    location: str


class CompanyUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    description: str | None = None
    website: str | None = None
    location: str