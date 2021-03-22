from fastapi import FastAPI, HTTPException
from app.repositories.initialization import player, frontend_loader
from app.routers import router
from app.infra.responses import HTMLResponse, JavascriptResponse, StyleSheetResponse

app = FastAPI()

app.include_router(router)


@app.get('/assets/js/{path:path}', response_class=JavascriptResponse)
def frontend_script(path: str):
  content = frontend_loader.get_script(path)

  if content is None:
    raise HTTPException(404)

  return JavascriptResponse(content)


@app.get('/assets/css/{path:path}', response_class=StyleSheetResponse)
def frontend_style(path: str):
  content = frontend_loader.get_style(path)

  if content is None:
    raise HTTPException(404)

  return StyleSheetResponse(content)


@app.get('/{path:path}', response_class=HTMLResponse)
def frontend(path: str):
  return HTMLResponse(frontend_loader.get_html(), media_type="text/html")


@app.get('/', response_class=HTMLResponse)
def index():
  return HTMLResponse(frontend_loader.get_html())


@app.on_event("shutdown")
def shutdown():
  player.close()
