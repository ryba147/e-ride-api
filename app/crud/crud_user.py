import uuid
from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.utils import get_password_hash
from app.models.user import User
from app.schemas.user import UserCreateSchema, UserUpdateSchema


class CRUDUser(CRUDBase[User, UserCreateSchema, UserUpdateSchema]):
    def get_by_email(self, db: Session, user_email: str) -> Optional[User]:
        return db.query(User).filter(User.email == user_email).first()

    def get_by_id(self, db: Session, user_id: uuid.UUID) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()

    def get_list(self, db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        return db.query(User).limit(limit).all()

    def create(self, db: Session, user_data: UserCreateSchema):
        hashed_password = get_password_hash(user_data.password)

        new_user = User(**user_data.dict())
        new_user.password = hashed_password

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user


user_crud = CRUDUser(User)
