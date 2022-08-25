from fastapi import FastAPI, Response, Request, status, HTTPException, Depends, APIRouter, File, UploadFile
from ..pydantic_schemas.user import CreateUser, User, UserOpt, UserUpdate
from ..repositories.userRepo import register, singleUser, updatUser, verification
from ..utils.oauth2 import get_current_user, verify_access_token
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from ..mails.email import send_email
from ..db.database import get_db


# templates
from fastapi.templating import Jinja2Templates




router = APIRouter(tags = ['User'])


@router.post('/Register', status_code=status.HTTP_201_CREATED, response_model=UserOpt)
async def new_user(user: User,  db: Session = Depends(get_db)):
    # send_email([user.email], user)

    return register(db=db,  user=user)



@router.get("/user/{id}", response_model=UserOpt)
async def get_user(id:int, db: Session=Depends(get_db), current_user:User= Depends(get_current_user)):
    return singleUser(db=db, id=id)


@router.put("/user/{id}", response_model=UserOpt)
async def update(id:int, user:UserUpdate, db: Session = Depends(get_db), current_user:User= Depends(get_current_user)):
    return updatUser(db=db, user=user, id=id, values=dict(user))

    
templates= Jinja2Templates(directory='templates')

@router.get("/verification", response_class=HTMLResponse)
async def verification_email(request: Request, token: str):
   return verification(token)
        
   return templates.TemplateResponse("verification.html", {"reqest": request, "username": user.username})