from typing import Any, List, Annotated
import datetime

from fastapi import APIRouter, Body, Depends, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get("/", response_model=list[schemas.EventInDBBase])
def get_event(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 4,
    address: str = None,
    tags: Annotated[list[str] | None, Query()] = None
) -> list[Any]:
    """
    Get all events.
    """
    return crud.event.get_filter(db, skip=skip, limit=limit, address=address, tags=tags)


@router.get("/get/{id_event}", response_model=schemas.EventInDBBase)
def get_event(
    db: Session = Depends(deps.get_db),
    *,
    id_event: int
) -> models.Event:
    """
    Get all events.
    """
    return crud.event.get(db, id_event)


@router.get("/find", response_model=list[schemas.EventInDBBase])
def find_event(
    db: Session = Depends(deps.get_db),
    *,
    text: str
) -> list[models.Event]:
    """
    Search events.
    """
    return crud.event.search_from_title(db=db, text=text)


@router.post("/create", response_model=schemas.EventInDBBase)
def create_event(
    *,
    db: Session = Depends(deps.get_db),
    event_in: schemas.CreateEvent
) -> models.Event:
    """
    Create new event.
    """
    event = crud.event.create(db=db, obj_in=event_in)
    return event


@router.put("/update/{id_event}", response_model=schemas.UpdateEvent)
def update_item(
    *,
    db: Session = Depends(deps.get_db),
    id_event: int,
    event_in: schemas.UpdateEvent,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an event.
    """
    event = crud.event.get(db=db, id=id_event)
    if not event:
        raise HTTPException(status_code=404, detail="Item not found")
    item = crud.event.update(db=db, db_obj=event, obj_in=event_in)
    return item


