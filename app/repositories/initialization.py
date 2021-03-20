from os.path import dirname, join
from yaml import safe_load
from app.infra.player import MidiPlayer
from app.infra.file_lookup import FileLookup
from atexit import register

with open(join(dirname(__file__), 'config.yaml')) as f:
  config: dict = safe_load(f)

player = MidiPlayer(128)
lookup = FileLookup(config.get('dir', join(dirname(__file__), '..', 'midis')))


@register
def close():
  player.close()
