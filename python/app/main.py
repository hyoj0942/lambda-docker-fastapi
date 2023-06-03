# python/app/main.py
from fastapi import FastAPI, APIRouter
from mangum import Mangum
from api.order import router as order_router

app = FastAPI(
    title="FastAPI Serverless",
    description="FastAPI를 활용한 서버리스",
    version="0.1.0",
    root_path="/v1",
)

api_router = APIRouter(prefix="/api")


@app.get("/test")
async def health_check():
    return {"code": 200, "message": "success", "data": None}


api_router.include_router(order_router)
app.include_router(api_router)

handler = Mangum(app)
