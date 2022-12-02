from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic_schemas.token import Token
from utils import oauth2, hashVerify
from models.user import User
from db.database import get_db



router = APIRouter(tags = ['Login'])

@router.post('/login', response_model=Token)
async def login_user(user_info: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_info.username).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials!")
    
    if not hashVerify.verify(user_info.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Password")

    token = oauth2.access_token(data={"users_id": user.id})

    return {"access_token": token, "token_type":"bearer"}