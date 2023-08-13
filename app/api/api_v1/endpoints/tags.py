from typing import List

from fastapi import APIRouter, Depends
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
    tag_in: schemas.Tag
) -> models.Tag:
    """
    Create new tag.
    """
    tag = crud.tag.create(db=db, obj_in=tag_in)
    return tag


@router.post("/remove", response_model=schemas.Tag)
def remove_tag(
    *,
    db: Session = Depends(deps.get_db),
    tag_in: schemas.Tag
) -> models.Tag:
    """
    Remove tag.
    """
    tag = crud.tag.remove(db=db, id=tag_in.name)
    return tag

