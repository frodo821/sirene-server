from os.path import join, exists, isdir
from typing import Optional, Tuple
from mimetypes import guess_type

from app.logger import get_logger

logger = get_logger()


class FrontendLoader:

  def __init__(self, base_path: str):
    self.base_path = base_path

  def get_file(self, path: str) -> Optional[Tuple[bytes, str]]:
    logger.info(f"looking up file {path} in {self.base_path}")

    file = join(self.base_path, path)

    if isdir(file):
      file = join(file, 'index.html')

    if not exists(file):
      logger.warning(f"File {file} not found!")
      return None

    logger.info(f"file {file} found")

    with open(file, 'rb') as f:
      return f.read(), guess_type(file)[0] or "application/octet-stream"
