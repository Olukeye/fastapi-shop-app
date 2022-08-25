from fastapi import Response, status, HTTPException, Depends
from ..utils.model import create_new_user, get_user_by_id, update_user, get_user_by_email, get_user_by_username
from ..utils.oauth2 import get_current_user, verify_access_token
from ..pydantic_schemas.user import *
from ..utils.hashVerify import hash
from sqlalchemy.orm import Session
from ..db.database import get_db
# from ..mails.email import send_email
from typing import Dict



def register(db: Session, user:User):
  
    hashed_password = hash(user.password)
    user.password = hashed_password
    # await send_email([user.email], user)
    return create_new_user(db=db, user=user)
    


def singleUser(db: Session, id:int):
    
    user = get_user_by_id(db=db, id=id)
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "User not found!")
    
    return user



def updatUser(db: Session, user:UserUpdate, id: int, values: Dict={}):
    
    updated = update_user(db=db, user=user, id=id, values=values)
    
    if updated  is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= "You can't perform this action!!")
    
    return updated 


async def verification(token: str):
    user = await verify_access_token(token, credentials_exception)
    if user and not user.verified:
        user.verified = True
        await user.save()
    
    return user