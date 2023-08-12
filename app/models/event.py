from typing import TYPE_CHECKING


from sqlalchemy import Boolean, Column, Integer, String, Enum, Float, Date, Time, Text, ARRAY, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=64), nullable=False)
    description = Column(Text)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    lon = Column(String, nullable=False, default="56.788751")
    lat = Column(String, nullable=False, default="60.475066")
    tags = Column(ARRAY(String), nullable=False)
    duration = Column(Integer, nullable=False, default=0)
    price = Column(Integer, nullable=False, default=0)
