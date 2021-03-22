from fastapi import FastAPI, HTTPException
from app.repositories.initialization import player
from app.routers import router
from app.routers.frontend import router as frontend_router

app = FastAPI()

app.include_router(router)
app.include_router(frontend_router)


@app.on_event("shutdown")
def shutdown():
  player.close()
