from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Tag])
def get_tags(
    db: Session = Depends(deps.get_db)
) -> list[models.Tag]:
    """
    Get all tags.
    """
    return crud.tag.get_multi(db)


@router.post("/create", response_model=schemas.Tag)
def create_tag(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.Tag
) -> models.Tag:
    """
    Create new tag.
    """
    tag = crud.tag.create(db=db, obj_in=item_in)
    return tag

