from fastapi import FastAPI, Response, requests, status, HTTPException, Depends, APIRouter, File, UploadFile
from ..pydantic_schemas.user import CreateUser, User, UserOpt, UserUpdate
from ..repositories.userRepo import register
from sqlalchemy.orm import Session
from ..db.database import get_db
from ..utils import oauth2


router = APIRouter(tags = ['User'])




