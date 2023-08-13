from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.FeedbackInDBBase])
def get_fb(
    db: Session = Depends(deps.get_db)
) -> list[models.Feedback]:
    """
    Get all feedback.
    """
    return crud.feedback.get_multi(db)


@router.get("/rating")
def get_rating(
    db: Session = Depends(deps.get_db),
    *,
    event_id: int
) -> float:
    """
    Get event rating.
    """
    feedbacks = crud.feedback.get_by_event_id(db, event_id)
    if feedbacks:
        n = 0
        count = 0
        for elem in feedbacks:
            count += 1
            n += elem.rating
        return round(n / count, 2)
    return 0


@router.post("/create", response_model=schemas.CreateFeedback)
def create_fb(
    *,
    db: Session = Depends(deps.get_db),
    fb_in: schemas.CreateFeedback
) -> models.Feedback:
    """
    Create new feedback.
    """
    fb = crud.feedback.create(db=db, obj_in=fb_in)
    return fb
