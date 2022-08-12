from sqlalchemy import Column, Integer, String, Boolean, BigInteger
from ..utils.date_stuff import create_customised_datetime
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import Session
from ..db.database import get_db, Base
from typing import Dict
from ..pydantic_schemas.user import CreateUser, User, UserOpt, UserUpdate


class User(Base):
    __tablename__= "users"
    id = Column(BigInteger, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    verified = Column(Boolean, server_default="False", nullable=False)
    # is_active = Column(String, server_default="False", nullable=False)
    role = Column(Boolean, nullable=False, server_default="False")
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)


def create_new_user(db: Session, user: CreateUser):
    
    newUser = User(username=user.username, email=user.email, password=user.password, verified=user.verified,
                   role=user.role, created_at=create_customised_datetime(), updated_at=create_customised_datetime())
    
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    
    return newUser

def get_user(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    return user
    
