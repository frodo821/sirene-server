from logging import (
  ERROR,
  INFO,
  NOTSET,
  WARNING,
  DEBUG,
  LogRecord,
  Logger,
  captureWarnings,
  getLogger as logging_getLogger,
  StreamHandler,
  Formatter,
  root,
)
from sys import _getframe, stderr
import sys
import colorama as c


def get_logger(name: str | None = None) -> Logger:
  if name is None:
    frame = _getframe(1)
    name = frame.f_globals.get('__name__', frame.f_code.co_qualname)

  return logging_getLogger(name)


class _Formatter(Formatter):

  def __init__(self) -> None:
    super().__init__((
      f'{c.Fore.LIGHTBLACK_EX}%(asctime)s{c.Fore.RESET}'
      f' - %(lc)s%(name)s{c.Fore.RESET}\t'
      f'[%(lc)s%(levelname)s{c.Fore.RESET}]\t'
      f'%(lc)s%(message)s{c.Fore.RESET}'
    ))

  def format(self, record: LogRecord) -> str:
    record.lc = self.get_lc(record)
    return super().format(record)

  def get_lc(self, record: LogRecord):
    no = record.levelno

    if no <= DEBUG:
      return c.Fore.LIGHTBLACK_EX
    if no <= INFO:
      return c.Fore.LIGHTWHITE_EX
    if no <= WARNING:
      return c.Fore.LIGHTYELLOW_EX
    if no <= ERROR:
      return c.Fore.LIGHTRED_EX
    return c.Fore.LIGHTMAGENTA_EX


def clear_external_logger_handlers():
  for l in root.manager.loggerDict.values():
    if isinstance(l, Logger):
      l.handlers.clear()
      l.level = NOTSET
      l.propagate = True
      l.disabled = False


def initialize(level: int = NOTSET):
  clear_external_logger_handlers()

  if sys.stderr.isatty():
    c.init(autoreset=True)

  ch = StreamHandler(stderr)
  ch.setLevel(level)
  ch.setFormatter(_Formatter())
  root.addHandler(ch)
  root.setLevel(level)

  get_logger().info('logger initialized.')

captureWarnings(True)
