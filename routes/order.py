from fastapi import FastAPI, Response, requests, status, HTTPException, Depends, APIRouter, File, UploadFile
from pydantic_schemas.order import *
from repositories.orderRepo import create_new_oder
from pydantic_schemas.order import *
from utils.oauth2 import get_current_user
from sqlalchemy.orm import Session
from db.database import get_db
from typing import List
import shutil

router = APIRouter(tags = ['Order'])

@router.post("/order")
async def new_order( order:CreateOrderModel, db: Session = Depends(get_db), user:int=Depends(get_current_user)):
    return create_new_oder(db=db, order=order, user=user)