from abc import ABC, abstractmethod
from app.domains.server.server import ServerStatus


class ServerRepositoryInterface:
  @abstractmethod
  def get_current_status(self) -> ServerStatus:
    pass
