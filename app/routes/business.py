from fastapi import FastAPI, Response, requests, status, HTTPException, Depends, APIRouter, File, UploadFile
from ..pydantic_schemas.business import CreateBis, Business, BusOpt
from ..repositories.busisnessRepo import create_business
from ..utils.oauth2 import get_current_user
from sqlalchemy.orm import Session
from ..db.database import get_db



router = APIRouter(tags = ['Business'])

@router.post("/business", status_code=status.HTTP_201_CREATED, response_model=BusOpt)
async def new_business(reg:CreateBis, db: Session = Depends(get_db), user:int = Depends(get_current_user)):
    return create_business(db=db, user=user, reg=reg)
