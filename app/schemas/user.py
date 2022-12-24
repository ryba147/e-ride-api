import uuid
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Roles(str, Enum):
    ADMIN = "ADMIN"
    DEFAULT = "DEFAULT"


class UserBaseSchema(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: str  # EmailStr
    is_active: bool = True
    role: Roles = Roles.DEFAULT


class UserCreateSchema(UserBaseSchema):
    password: str


class UserUpdateSchema(UserBaseSchema):
    pass


class UserResponse(UserBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
