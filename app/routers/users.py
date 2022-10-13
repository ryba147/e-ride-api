import uuid
from datetime import timedelta
from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth import (
    create_access_token,
    authenticate_user,
    get_current_active_user,
)
from app.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.crud.crud_user import (
    get_user_by_email,
    get_user_list,
    create_new_user,
    get_user_by_id,
)
from app.deps import get_db
from app.schemas.auth import Token
from app.schemas.user import UserResponse, CreateUserSchema

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/", response_model=List[UserResponse])
def list_users(limit: Optional[int] = 100, db: Session = Depends(get_db)):
    users = get_user_list(db, limit)
    return users


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: CreateUserSchema, db: Session = Depends(get_db)):
    user = get_user_by_email(db, user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists."
        )
    new_user = create_new_user(db, user_data)
    return new_user


@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: UserResponse = Depends(get_current_active_user)):
    return current_user


@router.get("/{email}", response_model=UserResponse)
def get_user(email: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with email {email} not found.",
        )
    return user


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found.",
        )
    return user
