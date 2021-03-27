from fastapi.routing import APIRouter
from app.routers.music import router as music_router
from app.routers.note import router as note_router
from app.routers.status import router as status_router
from app.routers.websocket import router as ws_router

router = APIRouter(prefix='/api/v1')
router.include_router(music_router)
router.include_router(note_router)
router.include_router(status_router)
router.include_router(ws_router)
