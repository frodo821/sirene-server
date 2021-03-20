from fastapi import FastAPI
import app.repositories.initialization  # noqa
from app.routers import router

app = FastAPI()

app.include_router(router)
