from fastapi import FastAPI
from src.routes.upload import files_router
from src.routes.tasks import tasks_router

app = FastAPI()

app.include_router(files_router)
app.include_router(tasks_router)
