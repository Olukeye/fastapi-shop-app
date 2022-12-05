from fastapi import Response, status, HTTPException, Depends
from utils.model import create_order
from pydantic_schemas.order import *
from sqlalchemy.orm import Session
from typing import Dict

def create_new_oder(db: Session, order:CreateOrderModel):
    data = create_order(db=db, order=order)
    return {
        "status":True,
        "message":"Success",
        "order": data
    }