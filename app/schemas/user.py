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


class UserCreateSchema(UserBaseSchema):
    password: str


class UserResponse(UserBaseSchema):
    id: Optional[uuid.UUID] = uuid.uuid4()
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
