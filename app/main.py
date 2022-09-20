from fastapi import FastAPI
from .models import user, product, business, category
from .routes import user, auth, business, product, category
from fastapi.middleware.cors import CORSMiddleware
from .db.database import Base, engine
from .config import settings


Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router)
app.include_router(auth.router)
app.include_router(business.router)
app.include_router(product.router)
app.include_router(category.router)



@app.get("/")
async def root():
    return {"message": "hello World!"}