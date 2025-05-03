from contextlib import asynccontextmanager
from os import environ
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.logger import get_logger, initialize, to_log_level
from app.repositories.environment import Environment
from app.routers import router
from app.routers.frontend import router as frontend_router

logger = get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
  initialize(to_log_level(environ.get('LOG_LEVEL', 'INFO')))
  get_logger('uvicorn.access').setLevel('ERROR')
  logger.info('initializing environment')
  env = Environment.get_instance()
  yield
  logger.info('shutting down server')
  env.player.close()


app = FastAPI(lifespan=lifespan)

app.add_middleware(
  CORSMiddleware,
  allow_origins='*',
  allow_methods=(
    'GET',
    'POST',
    'DELETE',
    'OPTIONS',
  ),
)

app.include_router(router)
app.include_router(frontend_router)
