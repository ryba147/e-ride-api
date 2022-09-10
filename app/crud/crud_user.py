import uuid
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.engine import Row

from app.auth import get_password_hash
from app.models.user import User
from app.schemas.user import CreateUser


def get_user_by_email(db: Session, user_email: str) -> Row:
    return db.query(User).filter(User.email == user_email).first()


def get_user_by_id(db: Session, user_id: uuid.UUID) -> Row:
    return db.query(User).filter(User.id == user_id).first()


def get_user_list(db: Session) -> List[Row]:
    return db.query(User).all()


def create_new_user(db: Session, user_data: CreateUser):
    hashed_password = get_password_hash(user_data.password)
    new_user = User(email=user_data.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
