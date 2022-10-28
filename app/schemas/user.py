import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.models.role import Role


class UserBaseSchema(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: str  # EmailStr
    is_active: bool = True
    role_id: uuid.UUID


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
