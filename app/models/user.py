from sqlalchemy import (
    Column,
    String,
    func,
    TIMESTAMP,
    ForeignKey,
    Boolean,
    text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.session import Base


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
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"))

    role = relationship("Role", back_populates="users")
    scooters = relationship("Scooter", back_populates="user")
