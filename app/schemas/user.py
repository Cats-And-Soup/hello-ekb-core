from typing import Optional

from pydantic import BaseModel, EmailStr

from app.shared.types import Roles


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    name: str
    role: Roles = Roles.user
    tags: list[str] = []
    image_src: str = "https://crypto.ru/wp-content/plugins/q-auth/assets/img/default-user.png"


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    name: str
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
