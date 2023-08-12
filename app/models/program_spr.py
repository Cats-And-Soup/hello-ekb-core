from typing import TYPE_CHECKING


from sqlalchemy import Boolean, Column, Integer, String, Enum, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.shared.types import Rating


class ProgramSpr(Base):
    __tablename__ = "programs_spr"
    __table_args__ = (
        PrimaryKeyConstraint('program_id', 'user_id'),
    )

    program_id = Column(Integer, ForeignKey('programs.id'))
    user_id = Column(Integer, ForeignKey("users.id"))
