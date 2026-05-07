from fastapi import FastAPI ,APIRouter

router_app = APIRouter()
@router_app.get("/test")
async def test():
    return {"message": "Hello World"}