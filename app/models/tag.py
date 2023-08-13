from sqlalchemy import Column, String

from app.db.database import Base


class Tag(Base):
    __tablename__ = "tags"

    name = Column(String, index=True, primary_key=True)
