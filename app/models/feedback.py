from typing import TYPE_CHECKING


from sqlalchemy import Boolean, Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.shared.types import Rating


class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, index=True, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    msg = Column(String(length=256))
    rating = Column(Enum(Rating), nullable=False)
