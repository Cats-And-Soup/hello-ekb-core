from typing import Any, List
from datetime import timedelta

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.api import deps
from app.core import security
from app.core.config import settings
from app.shared.types import Roles

router = APIRouter()


@router.post("/create", response_model=schemas.TokenPlus)
def create_user_open(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(...),
    email: EmailStr = Body(...),
    name: str = Body(None),
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )
    user = crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    user_in = schemas.UserCreate(password=password, email=email.lower(), name=name.lower())
    user = crud.user.create(db, obj_in=user_in)
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
        "id": user.id,
        "name": user.name
        }


@router.put("/update", response_model=schemas.User)
def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    email: EmailStr = Body(None),
    password: str = Body(None),
    name: str = Body(None),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = schemas.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if name is not None:
        user_in.name = name.lower()
    if email is not None:
        user_in.email = email.lower()
    user = crud.user.update(db, db_obj=current_user, obj_in=user_in)
    return user


@router.put("/add_manager", response_model=schemas.User)
def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    email: EmailStr = Body(None),
    current_user: models.User = Depends(deps.get_current_manager),
) -> Any:
    """
    Update own user.
    """
    user = crud.user.get_by_email(db, email=email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = crud.user.update(db, db_obj=user, obj_in={"role": Roles.manager})
    return user


@router.get("/me", response_model=schemas.User)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user
