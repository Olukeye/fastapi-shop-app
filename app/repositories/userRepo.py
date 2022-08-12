from fastapi import Response, status, HTTPException, Depends
from ..utils.model import create_new_user, get_user
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
    return get_user(db=db, id=id)