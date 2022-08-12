from sqlalchemy import Column, Integer, String, Boolean, BigInteger
from ..utils.date_stuff import create_customised_datetime
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import Session
from ..db.database import get_db, Base
from typing import Dict
from ..pydantic_schemas.user import *


class User(Base):
    __tablename__= "users"
    id = Column(BigInteger, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    verified = Column(String, server_default="False", nullable=False)
    # is_active = Column(String, server_default="False", nullable=False)
    role = Column(String, nullable=False)
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)


def create_new_user(db: Session, reg: CreateUser):
    
    newUser = User(username=reg.username, email=reg.email, password=reg.password, verified=reg.verified,
                   admin=reg.admin, created_at=reg.create_customised_datetime, updated_at=reg.create_customised_datetime)
    
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    
    return newUser
