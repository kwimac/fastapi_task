from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app import endpoints

app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(endpoints.customer_router, tags=["customer"], prefix="/api/customer")
app.include_router(endpoints.order_router, tags=["order"], prefix="/api/order")


@app.get("/api/healthchecker")
def root():
    return {"message": "Hello World"}
