from typing import Optional

from pydantic import BaseModel, EmailStr


class ProgramBase(BaseModel):
    user_id: int
    name:str = 'Название'


class CreateProgram(ProgramBase):
    pass


class UpdateProgram(ProgramBase):
    pass


class ProgramInDBBase(ProgramBase):
    id: int

    class Config:
        from_attributes = True


