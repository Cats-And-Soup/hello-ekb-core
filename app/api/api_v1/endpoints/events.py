from typing import Any, Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.api import deps

router = APIRouter()


@router.get("/", response_model=list[schemas.EventInDBBase])
def get_event(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 4,
    address: Annotated[str | None, Query(max_length=256)] = None,
    tags: Annotated[list[str] | None, Query()] = None,
    price: int = None,
    today: bool = 0
) -> list[Any]:
    """
    Get all events.
    """
    return crud.event.get_filter(db, skip=skip, limit=limit, address=address, tags=tags, price=price, today=today)


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
    text: Annotated[str | None, Query(max_length=64)]
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
def update_event(
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


