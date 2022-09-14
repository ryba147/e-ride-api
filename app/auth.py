import os
from datetime import timedelta, datetime
from typing import Union

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.crud.crud_user import get_user_by_email

# todo: move to config file!
from app.schemas.user import TokenData, User
from app.utils import verify_password

SIGN_SECRET_KEY = os.environ.get(
    "SIGN_SECRET_KEY",
    "e025ce978c17a012241a16ca1457e2d4c4f9d7e8f47c2cd2b5ac629c43c64db4",
)
SIGN_ALGORITHM = os.environ.get("SIGN_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
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
    encoded_jwt = jwt.encode(to_encode, SIGN_SECRET_KEY, algorithm=SIGN_ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SIGN_SECRET_KEY, algorithms=[SIGN_ALGORITHM])
        user_email: str = payload.get("sub", None)

        if user_email is None:
            raise credentials_exceptions
        token_data = TokenData(user_email)
    except JWTError:
        raise credentials_exceptions

    # todo: important
    from app.deps import get_db

    db = get_db()

    user = get_user_by_email(db, user_email)
    if user is None:
        raise credentials_exceptions
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user."
        )
    return current_user
