import os

from pydantic import BaseSettings

SQLALCHEMY_DATABASE_URL = os.environ.get(
    "SQLALCHEMY_DATABASE_URL",
    "postgresql+psycopg2://postgres:password@localhost:5432/vwire_db",
)

ACCESS_TOKEN_EXPIRE_MINUTES = 60
JWT_SECRET_KEY = os.environ.get(
    "JWT_SECRET_KEY",
    "e025ce978c17a012241a16ca1457e2d4c4f9d7e8f47c2cd2b5ac629c43c64db4",
)
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM", "HS256")


# class Settings(BaseSettings):
#     SQLALCHEMY_DATABASE_URL: str
#
#     JWT_SECRET_KEY: str
#     JWT_ALGORITHM: str
#     ACCESS_TOKEN_EXPIRE_MINUTES: int
