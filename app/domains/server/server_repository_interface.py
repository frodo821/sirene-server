from abc import ABC, abstractmethod


class ServerRepositoryInterface:
  @abstractmethod
  def get_current_status(self):
    pass
