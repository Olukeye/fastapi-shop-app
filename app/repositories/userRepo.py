from fastapi import Response, status, HTTPException, Depends
from ...utils.model import create_new_user
from ...pydantic_schemas.user import User
from ...utils.hashVerify import hash
from sqlalchemy.orm import Session
from ...db.database import get_db
from typing import Dict


def register(db: Session, reg:User):
    
    hashed_password = hash(user.password)
    user.password = hashed_password
    
    return create_new_user(db=db, reg=reg)