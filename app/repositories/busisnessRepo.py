from fastapi import Response, status, HTTPException, Depends
from ..utils.model import create_new_business, get_all_business, update_business
from ..pydantic_schemas.business import *
from sqlalchemy.orm import Session
from typing import Dict


def create_business(db: Session, user:int, reg:CreateBis):
    return create_new_business(db=db, user=user, reg=reg)


def allBusiness(db: Session):
    return get_all_business(db=db)


def updateBusiness(id: int, user:int,  edit: UpdateBizz, db: Session, values: Dict={}):
   update = update_business(id=id, db=db, edit=edit ,values=values)
   
   if not update:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = f"You can't perform this action!")
    
   elif update.user_id != user.id:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = f"Sorry you didn't create this!")
    
   return update
    
       