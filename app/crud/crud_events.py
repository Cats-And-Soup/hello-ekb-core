import datetime
from typing import List, Type

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.event import Event
from app.schemas.event import CreateEvent, UpdateEvent


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

    def search_from_title(self, db: Session, *, text: str) -> List[Type[Event]]:
        return db.query(self.model).filter(self.model.title.like(f"%{text}%")).all()

    def get_filter(
            self, db: Session,
            *,
            skip: int = 0,
            limit: int = 100,
            address: str | None = None,
            tags: set[str] | None = None,
            price: int | None = None,
            today: bool = False,
    ) -> List[Type[Event]]:
        query = db.query(self.model)
        if address is not None:
            query = query.filter_by(address=address)
        if price is not None:
            query = query.filter_by(price=price)
        if today:
            query = query.filter(self.model.start_datetime >= datetime.datetime.now().date())
        query = query.offset(skip).limit(limit)
        if tags is not None:
            query = query.all()
            tmp_query = query[::]
            for elem in tmp_query:
                if not all(list(map(lambda x: True if x in elem.tags else False, tags))):
                    query.remove(elem)
        else:
            query = query.all()
        return query


event = CRUDEvent(Event)
