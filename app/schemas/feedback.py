from pydantic import BaseModel

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

    class Config:
        from_attributes = True
