from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.tag import Tag
from app.schemas.tag import Tag as TagSchemas


class CRUDTag(CRUDBase[Tag, TagSchemas, TagSchemas]):
    def create(self, db: Session, *, obj_in: TagSchemas) -> Tag:
        db_obj = Tag(
            name=obj_in.name
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: str) -> Tag:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj


tag = CRUDTag(Tag)
