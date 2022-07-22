import uuid

from sqlalchemy.orm import Session

from app.models.user import User


def get_user(db: Session, user_id: uuid.UUID):
    # return db.query(User).filter(User.id == user_id).first()
    pass


def get_user_by_email(db: Session, user_email: str):
    return db.query(User).filter(User.email == user_email).first()
