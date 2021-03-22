from fastapi import FastAPI, Response
from app.repositories.initialization import player
from app.routers import router

app = FastAPI()

app.include_router(router)


@app.get('/assets/js/{path:path}')
def frontend_script(path: str):
  return Response(f"<h1>{path}</h1>", media_type="text/html")


@app.get('/assets/css/{path:path}')
def frontend_style(path: str):
  return Response(f"<h1>{path}</h1>", media_type="text/html")


@app.get('/{path:path}')
def frontend(path: str):
  return Response("<h1>Hello, World!</h1>", media_type="text/html")


@app.get('/')
def index():
  return Response("<h1>Hello, World!</h1>", media_type="text/html")


@app.on_event("shutdown")
def shutdown():
  player.close()
