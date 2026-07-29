from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr


class UserUpdate(BaseModel):
    model_config  = ConfigDict(from_attributes=True)

    name: str | None = None
    email: EmailStr | None = None