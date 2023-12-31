from sqlalchemy import Column, Integer, String, DateTime, Text, ARRAY

from app.db.database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=64), nullable=False)
    description = Column(Text)
    address = Column(String(length=256), nullable=False)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=False)
    lon = Column(String(length=64), nullable=False, default="56.788751")
    lat = Column(String(length=64), nullable=False, default="60.475066")
    tags = Column(ARRAY(String(length=64)), nullable=False)
    duration = Column(Integer, nullable=False, default=0)
    price = Column(Integer, nullable=False, default=0)
    image_src = Column(String, nullable=False, default="https://crypto.ru/wp-content/plugins/q-auth/assets/img/default-user.png")
