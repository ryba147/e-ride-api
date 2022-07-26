from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.crud_user import (
    get_user_by_email,
    get_user_list,
    create_new_user,
)
from app.deps import get_db
from app.schemas.user import User, CreateUser

router = APIRouter(
    prefix="/users", tags=["Users"],
)


@router.get("/", response_model=List[User])
def list_users(limit: Optional[int] = 100, db: Session = Depends(get_db)):
    users = get_user_list(db)[:limit]
    return users


@router.get("/{email}", response_model=User)
def get_user(email: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with email {email} not found."
        )
    return user


@router.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(user_data: CreateUser, db: Session = Depends(get_db)):
    user = get_user_by_email(db, user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists."
        )
    new_user = create_new_user(db, user_data)
    return new_user
#
#
# @router.get("/users/{user_id}", response_model=User)
# def get_user(user_id: uuid.UUID):
#     user = get_user_by_id(user_id)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"User with id {user_id} not found."
#         )
#     return user
