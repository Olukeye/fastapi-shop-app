from fastapi import Response, status, HTTPException, Depends
from ..utils.model import *
from ..pydantic_schemas.product import *
from sqlalchemy.orm import Session
from ..db.database import get_db
from typing import Dict



def newProduct(db: Session, prod:ProdCreate):
    return create_new_product(db=db, prod=prod)


def allProduct(db: Session):
    return get_allProducts(db=db)