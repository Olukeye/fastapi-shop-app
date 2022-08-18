from fastapi import FastAPI, Response, requests, status, HTTPException, Depends, APIRouter, File, UploadFile
from ..pydantic_schemas.business import CreateBis, Business, BusOpt, Allbiz, UpdateBizz
from ..repositories.busisnessRepo import create_business,  allBusiness, updateBusiness, singleBusiness
from ..utils.oauth2 import get_current_user, if_user_is_admin
from sqlalchemy.orm import Session
from ..db.database import get_db
from typing import List


router = APIRouter(tags = ['Business'])


@router.get("/allbusiness")
async def get_all(db: Session = Depends(get_db), user:int =Depends(get_current_user)):
    return allBusiness(db=db)


@router.post("/business", status_code=status.HTTP_201_CREATED)
async def new_business(reg:CreateBis, db: Session = Depends(get_db), user:int = Depends(if_user_is_admin)):
    return create_business(db=db, user=user, reg=reg)


@router.put("/updateBusiness/{id}",status_code=status.HTTP_200_OK)
async def business_update(id: int, edit:UpdateBizz, db: Session = Depends(get_db), user: int =Depends(if_user_is_admin)):
    return updateBusiness(id=id, edit=edit, db=db, user=user, values=dict(edit))


@router.get("/siglebusiness/{id}")
async def single_business(id: int, db: Session = Depends(get_db), user: int = Depends(get_current_user)):
    return singleBusiness(id=id, db=db)