from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from routes import user, auth, business, product, category, order
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()


origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def catch_exception_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=jsonable_encoder({"details": str(e)}))

app.middleware('http')(catch_exception_middleware)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(business.router)
app.include_router(product.router)
app.include_router(category.router)
app.include_router(order.router)


@app.get("/")
async def root():
    return {"message": "hello World!"}