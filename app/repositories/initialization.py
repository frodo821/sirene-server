from os.path import dirname, join, exists
from yaml import safe_load, safe_dump
from app.infra.frontend_loader import FrontendLoader
from app.infra.player import MidiPlayer
from app.infra.file_lookup import FileLookup

__all__ = ['frontend_loader', 'player', 'lookup']

config_path = join(dirname(__file__), '..', '..', 'config.yaml')

if not exists(config_path):
  with open(config_path, 'w', encoding='utf-8') as f:
    safe_dump(
        data={
            'frontend': {
                'base_path': './frontend/public',
            },
            'time_resolution': 128,
            'midi_dir': './midis',
        },
        stream=f,
        default_flow_style=False,
        indent=2,
        sort_keys=True)

with open(config_path) as f:
  config: dict = safe_load(f) or {}

frontend: dict = config.get('frontend', {})
experimentals: dict = config.get('experimentals', {})

frontend_loader = FrontendLoader(frontend.get('base_path'))

player = MidiPlayer(
    config.get('time_resolution', 128),
    use_experimental_arduino_driver=experimentals.get('next_gen_arduino_driver', False))

lookup = FileLookup(config.get('midi_dir', './midis'))
