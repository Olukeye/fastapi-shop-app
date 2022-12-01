from fastapi import Response, status, HTTPException, Depends
from utils.model import create_category
from pydantic_schemas.category import *
from sqlalchemy.orm import Session
from typing import Dict


def category(db: Session, cat:CreateCate):
    return create_category(db=db, cat=cat)