from fastapi import Response, status, HTTPException, Depends
from ..utils.model import create_new_business
from ..pydantic_schemas.business import *
from sqlalchemy.orm import Session
from typing import Dict


def create_business(db: Session, user:int, reg:CreateBis):
    return create_new_business(db=db, user=user, reg=reg)