from typing import Any, Dict, Optional, Union, Type

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
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


tag = CRUDTag(Tag)
