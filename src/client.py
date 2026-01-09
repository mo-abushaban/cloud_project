from fastapi import FastAPI
from src.routes.upload import files_router

app = FastAPI()

app.include_router(files_router)
