from typing import TYPE_CHECKING


from sqlalchemy import Boolean, Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.shared.types import Rating


class Program(Base):
    __tablename__ = "programs"

    id = Column(Integer, index=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(length=64), nullable=False, default="Название")
