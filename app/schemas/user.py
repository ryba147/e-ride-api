import uuid
from typing import Sequence, Optional

from pydantic import BaseModel


# todo: here

class User(BaseModel):
    id: Optional[uuid.UUID] = uuid.uuid4()
    first_name: Optional[str]
    last_name: Optional[str]
    email: str


class CreateUser(User):
    password: str


class ListUsers(BaseModel):
    user_list: Sequence[User]
