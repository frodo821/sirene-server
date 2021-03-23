from os.path import join, exists, isdir
from typing import Optional, Tuple
from mimetypes import guess_type


class FrontendLoader:
  def __init__(self, base_path: str):
    self.base_path = base_path

  def get_file(self, path: str) -> Optional[Tuple[bytes, str]]:
    file = join(self.base_path, path)

    if isdir(file):
      file = join(file, 'index.html')

    if not exists(file):
      return None

    with open(file, 'rb') as f:
      return f.read(), guess_type(file)[0]
