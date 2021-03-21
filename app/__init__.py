from fastapi import FastAPI
from app.repositories.initialization import player
from app.routers import router

app = FastAPI()

app.include_router(router)


@app.on_event("shutdown")
def shutdown():
  player.close()
