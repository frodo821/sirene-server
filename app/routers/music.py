from fastapi.routing import APIRouter

router = APIRouter(prefix='/musics')


@router.get('')
def get_music_list():
  pass


@router.get('/{music_id}')
def get_music(music_id: int):
  pass
