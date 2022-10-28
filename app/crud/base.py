import uuid
from typing import TypeVar, Generic, Type, Optional, Union, Dict, List

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import declarative_base, Session

ModelType = TypeVar("ModelType", bound=declarative_base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_by_id(self, db: Session, obj_id: uuid.UUID) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == obj_id).first()

    def get_list(self, db: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return (
            db.query(self.model).order_by(self.model.id).limit(limit).all()
        )  # .offset(skip)

    def create(self, db: Session, obj_data: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_data)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, obj_id: int) -> ModelType:
        db_obj = db.query(self.model).get(obj_id)
        db.delete(db_obj)
        db.commit()
        return db_obj
