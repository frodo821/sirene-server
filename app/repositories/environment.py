from pathlib import Path
from pydantic import BaseModel
from yaml import safe_load, safe_dump
from app.infra.frontend_loader import FrontendLoader
from app.infra.player import MidiPlayer
from app.infra.file_lookup import FileLookup
from app.logger import get_logger

__all__ = ['Environment']

ROOT_PATH = Path(__file__).parent.parent.parent.absolute()
logger = get_logger()


class FrontendConfig(BaseModel):
  base_path: str = str(ROOT_PATH / './frontend/public')


class ExperimentalConfig(BaseModel):
  next_gen_arduino_driver: bool = True
  debugging_devices: int = 0


class Configuration(BaseModel):
  frontend: FrontendConfig = FrontendConfig()
  experimentals: ExperimentalConfig = ExperimentalConfig()
  time_resolution: int = 128
  midi_dir: str = str(ROOT_PATH / './midis')


class Environment:
  CONFIG_PATH = ROOT_PATH / 'config.yaml'

  __instance: 'Environment | None' = None

  def __init__(self):
    self.config = self.load_config()

    self.frontend_loader = FrontendLoader(self.config.frontend.base_path)

    self.player = MidiPlayer(
      resolution=self.config.time_resolution,
      use_experimental_arduino_driver=self.config.experimentals.next_gen_arduino_driver,
      debugging_virtual_devices=self.config.experimentals.debugging_devices,
    )

    self.lookup = FileLookup(self.config.midi_dir)

  @classmethod
  def get_instance(cls) -> 'Environment':
    if cls.__instance is None:
      cls.__instance = Environment()
    return cls.__instance

  @classmethod
  def load_config(cls):
    if not cls.CONFIG_PATH.exists():
      logger.info(f"Config file not found. Creating a new one at {cls.CONFIG_PATH}")
      cls.initialize_config()

    with open(cls.CONFIG_PATH) as f:
      return Configuration.model_validate(safe_load(f) or {})

  @classmethod
  def initialize_config(cls):
    cls.CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(cls.CONFIG_PATH, 'w', encoding='utf-8') as f:
      safe_dump(
        data=Configuration().model_dump(mode='json'),
        stream=f,
        default_flow_style=False,
        indent=2,
        sort_keys=True,
      )
