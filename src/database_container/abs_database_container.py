import os

from container.abs_container import AbstractContainer

class DatabaseConnectionOpts:
  def __init__(
    self,
    database: str,
    host: str | None,
    user: str | None,
    password: str | None,
    port: int | None
  ):
    self.database = database
    self.host = os.getenv("DB_HOST") or host
    self.user = os.getenv("DB_USER") or user
    self.password = os.getenv("DB_PASS") or password
    self.port = os.getenv("DB_PORT") or port


class AbstractDatabaseContainer:
  def __init__(self, container: AbstractContainer, connection_opts: DatabaseConnectionOpts):
    self.__container = container
    self.__connection_opts = connection_opts

  def create(self) -> None:
    self.__container.create(self._enviroment(self.__connection_opts))

  def connect(self) -> None:
    self.__container.execute(self._connect_command(self.__connection_opts))

  def _connect_command(self, _: DatabaseConnectionOpts) -> str:
    raise NotImplemented()

  def _enviroment(self, _: DatabaseConnectionOpts) -> list[str]:
    raise NotImplemented()
