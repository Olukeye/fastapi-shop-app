from fastapi import Response, status, HTTPException, Depends
from ..utils.model import create_new_user, get_user_by_id, update_user
from ..pydantic_schemas.user import *
from ..utils.hashVerify import hash
from sqlalchemy.orm import Session
from ..db.database import get_db
from typing import Dict


def register(db: Session, user:User):
    
    hashed_password = hash(user.password)
    user.password = hashed_password
    
    return create_new_user(db=db, user=user)



def singleUser(db: Session, id:int):
    return get_user_by_id(db=db, id=id)



def updatUser(db: Session, user:UserUpdate, id: int, values: Dict={}):
    
    updated = update_user(db=db, user=user, id=id, values=values)
    
    # if updated  is None:
    #     raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= "You can't perform this action!!")
        
    return updated 