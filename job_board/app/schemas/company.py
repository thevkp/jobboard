from pydantic import BaseModel, ConfigDict


class CompanyCreate(BaseModel):
    title: str
    description: str | None = None
    website: str | None = None
    location: str | None


class CompanyRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str | None
    description: str | None = None
    website: str | None = None
    location: str | None


class CompanyUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str | None
    description: str | None = None
    website: str | None = None
    location: str