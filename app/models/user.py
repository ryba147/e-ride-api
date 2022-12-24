from sqlalchemy import (
    Column,
    String,
    func,
    TIMESTAMP,
    Boolean,
    text,
)
from sqlalchemy.dialects.postgresql import UUID, ENUM
from sqlalchemy.orm import relationship

from app.database.session import Base
from app.schemas.user import Roles


class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        server_default=text("uuid_generate_v4()"),
    )
    email = Column(String(64), unique=True)
    first_name = Column(String(64))
    last_name = Column(String(64))
    password = Column(String(128))
    is_active = Column(Boolean, default=True)
    role = Column(ENUM(Roles), default=Roles.DEFAULT)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    scooters = relationship("Scooter", back_populates="user")
