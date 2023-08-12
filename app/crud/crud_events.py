from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.event import Event
from app.schemas.event import EventInDBBase, CreateEvent, UpdateEvent


class CRUDEvent(CRUDBase[Event, CreateEvent, UpdateEvent]):
    def create_with_owner(
        self, db: Session, *, obj_in: CreateEvent, owner_id: int
    ) -> Event:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


event = CRUDEvent(Event)
