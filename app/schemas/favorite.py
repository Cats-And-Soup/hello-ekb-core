from typing import Optional

from pydantic import BaseModel, EmailStr


class Favorite(BaseModel):
    event_id: int
    user_id: int

