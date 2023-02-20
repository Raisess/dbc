import os

from common.exceptions import DatabaseConnectionParamNotProvidedException
from core.containers.abs_container import AbstractContainer

class DatabaseConnectionOpts:
  def __init__(
    self,
    database: str = os.getenv("DB_NAME") or "mydatabase",
    port: str | int = os.getenv("DB_PORT") or 1234,
    user: str = os.getenv("DB_USER") or "root",
    password: str = os.getenv("DB_PASS") or "mysecretpassword"
  ):
    self.database = database
    self.port = int(port)
    self.user = user
    self.password = password


class AbstractDatabaseContainer:
  def __init__(
    self,
    container: AbstractContainer,
    connection_opts: DatabaseConnectionOpts = DatabaseConnectionOpts()
  ):
    self.__container = container
    self.__connection_opts = connection_opts
    self.__container.bind(self.__connection_opts.port)

  def create(self) -> None:
    self.__container.create(self._enviroment(self.__connection_opts))

  def connect(self) -> None:
    self.__container.execute(self._connect_command(self.__connection_opts))

  def _connect_command(self, _: DatabaseConnectionOpts) -> str:
    raise NotImplemented()

  def _enviroment(self, _: DatabaseConnectionOpts) -> list[str]:
    raise NotImplemented()
