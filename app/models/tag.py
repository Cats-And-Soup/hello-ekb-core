from typing import TYPE_CHECKING


from sqlalchemy import Boolean, Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.shared.types import Roles


class Tag(Base):
    __tablename__ = "tags"

    name = Column(String, index=True, primary_key=True)
