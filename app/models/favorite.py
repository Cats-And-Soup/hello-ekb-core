from typing import TYPE_CHECKING


from sqlalchemy import Boolean, Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.shared.types import Rating


class Favorite(Base):
    __tablename__ = "favorites"

    event_id = Column(Integer, ForeignKey("events.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
