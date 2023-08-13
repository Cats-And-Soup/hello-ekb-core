from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint

from app.db.database import Base


class Favorite(Base):
    __tablename__ = "favorites"
    __table_args__ = (
        PrimaryKeyConstraint('event_id', 'user_id'),
    )

    event_id = Column(Integer, ForeignKey("events.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
