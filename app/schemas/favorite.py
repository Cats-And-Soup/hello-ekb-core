from pydantic import BaseModel


class Favorite(BaseModel):
    event_id: int
    user_id: int

