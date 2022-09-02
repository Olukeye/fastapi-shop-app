from fastapi import FastAPI, Response, requests, status, HTTPException, Depends, APIRouter, File, UploadFile
from ..pydantic_schemas.product import *
from ..repositories.productRepo import newProduct, allProduct, singleProduct, updateProduct, deleteProduct
from ..pydantic_schemas.product import *
from ..utils.oauth2 import get_current_user, if_user_is_admin
from sqlalchemy.orm import Session
from ..db.database import get_db
from typing import List
import shutil

router = APIRouter(tags = ['Product'])


@router.get("/allProduct")
async def get_Products(db: Session = Depends(get_db), user: int = Depends(get_current_user)):
     return allProduct(db=db)


@router.post("/product",status_code=status.HTTP_201_CREATED, response_model=ProdOpt)
async def createProduct( prod:ProdCreate, db: Session = Depends(get_db),file: UploadFile = File(...), user: int = Depends(if_user_is_admin)):
     
     with open("media/"+file.filename, "wb") as image:
        shutil.copyfileobj(file.file, image)
        
     url = str("media/"+file.filename)
     
     return newProduct(db=db,file=file, prod=prod)


@router.get("/singleProduct/{id}")
async def single_product(id: int, db: Session = Depends(get_db), user: int = Depends(get_current_user)):
     return singleProduct(id=id, db=db)


@router.delete("/deleteProduct/{id}", status_code = status.HTTP_204_NO_CONTENT)
async def delete_prod(id: int, db: Session = Depends(get_db), user: int = Depends(if_user_is_admin)):
     return deleteProduct(id=id, user=user, db=db)


@router.put("/editproduct/{id}", status_code=status.HTTP_200_OK)
async def update_product(id: int, edit: ProdUpdate, db: Session = Depends(get_db), user: int = Depends(if_user_is_admin)):
     return updateProduct(id=id, db=db, edit=edit, values=dict(edit))
