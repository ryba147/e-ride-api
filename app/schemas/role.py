import uuid

from pydantic import BaseModel


class RoleBaseSchema(BaseModel):
    name: str
    description: str


class RoleCreateSchema(RoleBaseSchema):
    code: str


class RoleUpdateSchema(RoleBaseSchema):
    pass


class RoleResponse(RoleBaseSchema):
    id: uuid.UUID
    code: str

    class Config:
        orm_mode = True
