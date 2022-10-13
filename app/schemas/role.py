import uuid

from pydantic import BaseModel


class RoleBaseSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class RoleCreateSchema(RoleBaseSchema):
    pass


class RoleUpdate(RoleBaseSchema):
    user_id: uuid.UUID
