from fastapi import APIRouter, HTTPException, Response
from app.repositories.initialization import frontend_loader

router = APIRouter()


@router.get('/{path:path}')
def frontend(path: str):
  content = frontend_loader.get_file(path)
  if content is None:
    raise HTTPException(404)
  return Response(content[0], media_type=content[1])


@router.get('/')
def index():
  content = frontend_loader.get_file('')
  if content is None:
    raise HTTPException(404)
  return Response(content[0], media_type=content[1])
