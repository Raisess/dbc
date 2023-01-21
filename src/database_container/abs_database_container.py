import os

from container.abs_container import AbstractContainer

class VarNotProvidedException(Exception):
  def __init__(self, var_name: str):
    super().__init__(f"{var_name} not provided")


class DatabaseConnectionOpts:
  def __init__(
    self,
    database: str = os.getenv("DB_NAME"),
    host: str = os.getenv("DB_HOST"),
    user: str = os.getenv("DB_USER"),
    password: str = os.getenv("DB_PASS"),
    port: str | int = os.getenv("DB_PORT")
  ):
    if not database:
      raise VarNotProvidedException("DB_NAME")
    if not host:
      raise VarNotProvidedException("DB_HOST")
    if not port:
      raise VarNotProvidedException("DB_PORT")
    if not user:
      raise VarNotProvidedException("DB_USER")
    if not password:
      raise VarNotProvidedException("DB_PASS")

    self.database = database
    self.host = host
    self.user = user
    self.password = password
    self.port = int(port)


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
