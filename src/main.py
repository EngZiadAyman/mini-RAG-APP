from fastapi import FastAPI

from routes import base, data

app = FastAPI()
app.include_router(base.router_app)
app.include_router(data.router_app)

