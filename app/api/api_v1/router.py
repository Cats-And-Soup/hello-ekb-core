from fastapi import APIRouter

from app.api.api_v1.endpoints import users, login, events, tags, feedbacks, favorites

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(events.router, prefix="/events", tags=["events"])
api_router.include_router(tags.router, prefix='/tags', tags=['tags'])
api_router.include_router(feedbacks.router, prefix='/feedback', tags=['feedback'])
api_router.include_router(favorites.router, prefix='/favorites', tags=['favorites'])
