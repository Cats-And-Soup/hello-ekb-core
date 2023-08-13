from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Favorite])
def get_favorites(
    db: Session = Depends(deps.get_db), *, user_id: int
) -> list[models.Favorite]:
    """
    Get all favorites.
    """
    return crud.favorite.get_by_user_id(db, user_id)


@router.post("/create")
def create_favorite(
    *,
    db: Session = Depends(deps.get_db),
    fb_in: schemas.Favorite
) -> list[int]:
    """
    Create new favorite.
    """
    fb = crud.favorite.create(db=db, obj_in=fb_in)
    events_id = crud.favorite.get_by_user_id(db=db, user_id=fb_in.user_id)
    return list(map(lambda x: x.event_id, events_id))


@router.post("/remove", response_model=schemas.Favorite)
def remove_favorite(
    *,
    db: Session = Depends(deps.get_db),
    fb_in: schemas.Favorite
) -> models.Favorite:
    """
    Remove new favorite.
    """
    fb = crud.favorite.remove_(db=db, event_id=fb_in.event_id, user_id=fb_in.user_id)
    return fb
