from fastapi.routing import APIRouter
from app.routers.music import router as music_router
from app.routers.note import router as note_router
from app.routers.status import router as status_router

router = APIRouter()
router.include_router(music_router)
router.include_router(note_router)
router.include_router(status_router)
