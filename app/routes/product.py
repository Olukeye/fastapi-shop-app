from fastapi import FastAPI, Response, requests, status, HTTPException, Depends, APIRouter, File, UploadFile
from ..pydantic_schemas.product import *
from ..repositories.productRepo import newProduct, allProduct
from ..pydantic_schemas.product import *
from ..utils.oauth2 import get_current_user, if_user_is_admin
from sqlalchemy.orm import Session
from ..db.database import get_db
from typing import List


router = APIRouter(tags = ['Product'])


@router.post("/product")
async def createProduct( prod:ProdCreate, db: Session = Depends(get_db), user: int = Depends(if_user_is_admin)):
     return newProduct(db=db, prod=prod)


@router.get("/allProduct")
async def get_Products(db: Session = Depends(get_db), user: int = Depends(get_current_user)):
     return allProduct(db=db)