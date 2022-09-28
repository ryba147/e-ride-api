import uuid
from typing import Optional, Union

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: str  # Optional[EmailStr] = None
    # phone_number: str
    is_active: bool = None


class User(UserBase):
    id: Optional[uuid.UUID] = uuid.uuid4()
    roles_name: str

    class Config:
        orm_mode = True


class CreateUser(UserBase):
    password: str
