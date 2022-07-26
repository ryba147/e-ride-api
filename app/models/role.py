from app.database.session import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.dialects.postgresql import UUID


class Role(Base):
    __tablename__ = "roles"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String(64))

    users = relationship("User", back_populates="role")
