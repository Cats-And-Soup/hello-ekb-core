from sqlalchemy import Column, Integer, String, Enum, ForeignKey, PrimaryKeyConstraint

from app.db.database import Base
from app.shared.types import Rating


class Feedback(Base):
    __tablename__ = "feedbacks"
    __table_args__ = (
        PrimaryKeyConstraint('event_id', 'user_id'),
    )

    event_id = Column(Integer, ForeignKey("events.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    msg = Column(String(length=256))
    rating = Column(Enum(Rating), nullable=False)
