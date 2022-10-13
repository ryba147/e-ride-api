from app.database.session import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    String,
    text,
)
from sqlalchemy.dialects.postgresql import UUID


class Role(Base):
    __tablename__ = "roles"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        server_default=text("uuid_generate_v4()"),
    )
    name = Column(String(64))
    code = Column(String(64))

    users = relationship("User", back_populates="role")
