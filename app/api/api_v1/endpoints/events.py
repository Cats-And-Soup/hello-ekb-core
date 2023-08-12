from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import models, schemas
from app.crud import crud_user as crud
from app.api import deps
from app.core.config import settings

router = APIRouter()
