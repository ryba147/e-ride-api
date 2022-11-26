import uuid

from pydantic import BaseModel


class ScooterBaseSchema(BaseModel):
    code: str
    is_active: bool = True
    user_id: uuid.UUID = None


# class AssignScooterToUser(BaseModel):
#     scooter_id: uuid.UUID
#     user_id: uuid.UUID


class ScooterCreateSchema(ScooterBaseSchema):
    code: str


class ScooterUpdateSchema(ScooterBaseSchema):
    pass


class ScooterResponse(ScooterBaseSchema):
    id: uuid.UUID

    class Config:
        orm_mode = True
