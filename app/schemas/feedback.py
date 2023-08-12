from typing import Optional

from pydantic import BaseModel, EmailStr

from app.shared.types import Rating


# Shared properties
class FeedbackBase(BaseModel):
    msg: str
    rating: Rating
    event_id: int
    user_id: int


class CreateFeedback(FeedbackBase):
    pass


class UpdateFeedback(FeedbackBase):
    pass


class FeedbackInDBBase(FeedbackBase):
    id: int

    class Config:
        from_attributes = True
