from fastapi import FastAPI
from .models import user, business, product, category
from .routes import user, business, product, category
from .db.database import get_db, Base
from .config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "hello World!"}