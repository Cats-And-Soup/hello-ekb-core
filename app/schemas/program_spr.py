from typing import Optional

from pydantic import BaseModel, EmailStr


class ProgramSpr(BaseModel):
    event_id: int
    user_id: int

