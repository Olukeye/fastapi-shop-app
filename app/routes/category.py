from fastapi import FastAPI, Response, requests, status, HTTPException, Depends, APIRouter, File, UploadFile
from ..pydantic_schemas.category import CreateCate
from ..repositories.categoryRepo import category
from ..utils.oauth2 import if_user_is_admin
from sqlalchemy.orm import Session
from ..db.database import get_db
from typing import List


router = APIRouter(tags = ['Category'])



@router.post("/newCat")
async def newCategory(cat:CreateCate, db: Session = Depends(get_db), user: int = Depends(if_user_is_admin)):
    return category(db=db, cat=cat)