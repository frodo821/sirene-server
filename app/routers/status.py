from fastapi.routing import APIRouter
from app.usecases.get_server_status import GetServerStatus
from app.repositories.server import ServerRepository, ServerStatus
from app.repositories.initialization import player, lookup

router = APIRouter(prefix='/status')


@router.get('', response_model=ServerStatus)
def get_status():
  status = GetServerStatus(
      ServerRepository(player, lookup)
  ).execute()
  return dict(status)
