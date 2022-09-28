import uuid

from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class RoleCreate(RoleBase):
    pass


class RoleUpdate(RoleBase):
    user_id: uuid.UUID
