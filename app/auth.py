from datetime import timedelta, datetime
from typing import Union

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.config import JWT_SECRET_KEY, JWT_ALGORITHM
from app.crud.crud_user import user_crud
from app.schemas.auth import TokenData

from app.schemas.user import UserResponse
from app.utils import verify_password
from app.deps import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")


def authenticate_user(db: Session, email: str, password: str):
    user = user_crud.get_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt


async def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    credentials_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        user_email: str = payload.get("sub", None)

        if user_email is None:
            raise credentials_exceptions
        token_data = TokenData(user_email=user_email)
    except JWTError:
        raise credentials_exceptions

    user = user_crud.get_by_email(db, token_data.user_email)
    if user is None:
        raise credentials_exceptions
    return user


async def get_current_active_user(
    current_user: UserResponse = Depends(get_current_user),
):
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user."
        )
    return current_user
