import uuid
from typing import Optional, Union

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: str  # Optional[EmailStr] = None
    # phone_number: str
    is_active: bool


class User(UserBase):
    id: Optional[uuid.UUID] = uuid.uuid4()

    class Config:
        orm_mode = True


class CreateUser(UserBase):
    password: str


# todo: pass as body. better way.
class UserCredentials(BaseModel):
    email: str
    password: str


# todo: move to separate file
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_email: Union[str, None] = None
