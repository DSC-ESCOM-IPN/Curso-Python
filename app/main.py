from app.api.api import api_router
from fastapi import FastAPI

app = FastAPI(title="FastAPI Proyecto DSC ESCOM")

app.include_router(api_router)
