from fastapi.routing import APIRouter

router = APIRouter(prefix='/status')


@router.get('')
def get_status(self):
  pass
