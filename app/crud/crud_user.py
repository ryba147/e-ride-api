import uuid
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.engine import Row

from app.models.user import User


def get_user_by_email(db: Session, user_email: str) -> Row:
    return db.query(User).filter(User.email == user_email).first()


def get_user_list(db: Session) -> List[Row]:
    return db.query(User).all()
