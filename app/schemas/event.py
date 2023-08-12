import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class BaseEvent(BaseModel):
    title: str
    description: str = None
    date: datetime.date
    time: datetime.time
    address: str
    lon: str
    lat: str
    image_src: str = "https://crypto.ru/wp-content/plugins/q-auth/assets/img/default-user.png"
    tags: list[str]
    duration: int = 0
    price: int = 0


class EventInDBBase(BaseEvent):
    id: Optional[int] = None

    class Config:
        from_attributes = True


class CreateEvent(BaseEvent):
    pass


class UpdateEvent(BaseEvent):
    pass

