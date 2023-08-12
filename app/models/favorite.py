from typing import TYPE_CHECKING


from sqlalchemy import Boolean, Column, Integer, String, Enum, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.shared.types import Rating


class Favorite(Base):
    __tablename__ = "favorites"
    __table_args__ = (
        PrimaryKeyConstraint('event_id', 'user_id'),
    )

    event_id = Column(Integer, ForeignKey("events.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
