from glob import glob
from os.path import join
from app.domains.midi import MidiFile
from typing import Optional, List


class FileLookup:
  dir: str
  files: List[MidiFile]

  def __init__(self, path: str):
    paths = glob(join(path, '*.mid'), recursive=False)
    self.dir = path
    self.files = [MidiFile(idx, path) for idx, path in enumerate(paths)]

  def lookup(self, id: int) -> Optional[MidiFile]:
    if not self.files[id:]:
      return None
    return self.files[id]
