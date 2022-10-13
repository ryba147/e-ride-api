from typing import TypeVar, Generic, Type, Any, Optional

from pydantic import BaseModel
from sqlalchemy.orm import declarative_base, Session

ModelType = TypeVar("ModelType", bound=declarative_base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, obj_id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == obj_id).first()

    def get_list(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(self.model).limit(limit).all()

    def create(self, db: Session, *, obj_data: CreateSchemaType):
        db_obj = self.model(**obj_data.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
