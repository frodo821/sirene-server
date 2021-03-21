from app.domains.server.server_repository_interface import ServerRepositoryInterface


class GetServerStatus:
  def __init__(self, server_repository: ServerRepositoryInterface):
    self.server_repository = server_repository

  def execute(self):
    return self.server_repository.get_current_status()
