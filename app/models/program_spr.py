from typing import TYPE_CHECKING


from sqlalchemy import Boolean, Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.shared.types import Rating


class ProgramSpr(Base):
    __tablename__ = "programs_spr"

    program_id = Column(Integer, ForeignKey('program.id'))
    user_id = Column(Integer, ForeignKey("users.id"))
