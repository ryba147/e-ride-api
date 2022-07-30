from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    func,
    select,
    text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, column_property
from sqlalchemy.ext.hybrid import hybrid_property

from app.database.session import Base
from app.models.user import User


class Scooter(Base):
    __tablename__ = "scooters"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        server_default=text("uuid_generate_v4()"),
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"))

    user = relationship("User", back_populates="scooters")
