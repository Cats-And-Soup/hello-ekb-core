from sqlalchemy import Column, Integer, String, Enum, ARRAY

from app.db.database import Base
from app.shared.types import Roles


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(length=128), unique=True, index=True, nullable=False)
    name = Column(String(length=64), nullable=False)
    hashed_password = Column(String, nullable=False)
    tags = Column(ARRAY(String(length=64)), nullable=False, default=[])
    role = Column(Enum(Roles), default=Roles.user)
    image_src = Column(String(length=128), nullable=False,
                       default="https://crypto.ru/wp-content/plugins/q-auth/assets/img/default-user.png")
