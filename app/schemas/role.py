import uuid

from pydantic import BaseModel


class RoleBaseSchema(BaseModel):
    name: str
    code: str


class RoleCreateSchema(RoleBaseSchema):
    pass


class RoleUpdateSchema(RoleBaseSchema):
    # user_id: uuid.UUID
    pass


class RoleResponse(RoleBaseSchema):
    id: uuid.UUID

    class Config:
        orm_mode = True
