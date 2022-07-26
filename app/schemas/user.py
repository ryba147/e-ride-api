import uuid
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: str  # Optional[EmailStr] = None
    # phone_number: str


class User(UserBase):
    id: Optional[uuid.UUID] = uuid.uuid4()

    class Config:
        orm_mode = True


class CreateUser(UserBase):
    password: str
