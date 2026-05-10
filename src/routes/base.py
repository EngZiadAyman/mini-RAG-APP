from fastapi import FastAPI ,APIRouter,Depends
from helpers.config import Config, get_config


router_app = APIRouter()
@router_app.get("/test")
async def test(config: Config = Depends(get_config)):
    

    return {"message": "success",
            "app_name": config.APP_NAME,
            "app_version": config.APP_VERSION}