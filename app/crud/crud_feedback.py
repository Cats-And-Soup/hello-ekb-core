from typing import List, Type, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.feedback import Feedback
from app.schemas.feedback import FeedbackInDBBase, CreateFeedback, UpdateFeedback


class CRUDFeedback(CRUDBase[Feedback, CreateFeedback, UpdateFeedback]):
    def get_by_event_id(self, db: Session, event_id: int) -> list[Type[Feedback]]:
        return db.query(self.model).filter(self.model.event_id == event_id).all()


feedback = CRUDFeedback(Feedback)
