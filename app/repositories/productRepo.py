from fastapi import Response, status, HTTPException, Depends, File, UploadFile
from ..utils.oauth2 import get_current_user, if_user_is_admin
from ..utils.model import *
from ..pydantic_schemas.product import *
from sqlalchemy.orm import Session
from ..db.database import get_db
from typing import Dict



def allProduct(db: Session):
    return get_allProducts(db=db)


def newProduct(db: Session, prod:ProdCreate):
    return create_new_product(db=db, prod=prod)


def singleProduct(id: int, db: Session):
    products = get_single_product(id=id, db=db)
    
    if not products:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Product not found!")
    
    return products


def updateProduct(id: int, edit: ProdUpdate, db: Session, values: Dict={}):
    edited = update_product(id=id, db=db, edit=edit, values=values)
    
    if not edited:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = f"You can't perform this action!")
    
    return edited


def deleteProduct(id: int, db: Session, user: int):
    
    destroy = delete_product(id=id, user=user, db=db)
    
    if not destroy:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,  detail=f"Product id:{id} does not exist!")
    
    return destroy