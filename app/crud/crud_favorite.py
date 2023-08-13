from typing import Type
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.favorite import Favorite
from app.schemas.favorite import Favorite as FavoriteSchema


class CRUDFavorite(CRUDBase[Favorite, FavoriteSchema, FavoriteSchema]):
    def get_by_user_id(self, db: Session, user_id: int) -> list[Type[Favorite]]:
        return db.query(self.model).filter(self.model.user_id == user_id).all()

    def remove_(self, db: Session, *, user_id: int, event_id: int) -> Favorite | None:
        obj = db.query(self.model).filter(self.model.user_id == user_id, self.model.event_id == event_id).first()
        db.delete(obj)
        db.commit()
        return obj


favorite = CRUDFavorite(Favorite)
