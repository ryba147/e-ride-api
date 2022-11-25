from sqlalchemy import (
    Column,
    String,
    Boolean,
    ForeignKey,
    text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.session import Base


class Scooter(Base):
    __tablename__ = "scooters"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        server_default=text("uuid_generate_v4()"),
    )
    code = Column(String(64), nullable=False, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"))

    role = relationship("Role", back_populates="users")

    # trip_started_at =
    # last_location =
    # battery_percentage =
