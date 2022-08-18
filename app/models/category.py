from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey
from ..pydantic_schemas.category import CreateCate
from ..utils.date_stuff import create_customised_datetime
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from ..db.database import get_db, Base
from sqlalchemy.orm import Session
from typing import Dict, Optional


class Category(Base):
    __tablename__ = 'category'

    id = Column(BigInteger, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    created_at = Column(String, nullable=False, server_default=text('now()'))
    updated_at = Column(String, nullable=False, server_default=text('now()'))
    
    


def create_category(db: Session, cat: CreateCate):
    categ = Category(name=cat.name, created_at=create_customised_datetime(),updated_at=create_customised_datetime())
    
    db.add(categ)
    db.commit()
    db.refresh(categ)
    
    return categ