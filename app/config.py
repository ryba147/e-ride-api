import os

from pydantic import BaseSettings

import os
db_user = os.environ.get("CLOUD_SQL_USERNAME")
db_password = os.environ.get("CLOUD_SQL_PASSWORD")
db_name = os.environ.get("CLOUD_SQL_DATABASE_NAME")
connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")


SQLALCHEMY_DATABASE_URL = os.environ.get(
    "SQLALCHEMY_DATABASE_URL",
    # "postgresql+psycopg2://postgres:password@localhost:5432/vwire_db",
    # "postgresql+psycopg2://postgres:TQy3JCICG1pz9jY@@localhost:5432/vwire_db",
    f"postgresql+psycopg2://{db_user}:{db_password}@/vwire_db",
    # "postgresql+psycopg2://localhost/vwire_db?user=postgres&password=TQy3JCICG1pz9jY@",
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
