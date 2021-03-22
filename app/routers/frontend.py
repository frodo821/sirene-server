from fastapi import APIRouter, HTTPException
from app.repositories.initialization import frontend_loader
from app.infra.responses import HTMLResponse, JavascriptResponse, StyleSheetResponse

router = APIRouter()


@router.get('/assets/js/{path:path}', response_class=JavascriptResponse)
def frontend_script(path: str):
  content = frontend_loader.get_script(path)

  if content is None:
    raise HTTPException(404)

  return JavascriptResponse(content)


@router.get('/assets/css/{path:path}', response_class=StyleSheetResponse)
def frontend_style(path: str):
  content = frontend_loader.get_style(path)

  if content is None:
    raise HTTPException(404)

  return StyleSheetResponse(content)


@router.get('/{path:path}', response_class=HTMLResponse)
def frontend(path: str):
  return HTMLResponse(frontend_loader.get_html(), media_type="text/html")


@router.get('/', response_class=HTMLResponse)
def index():
  return HTMLResponse(frontend_loader.get_html())
