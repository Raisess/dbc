from core.containers.abs_container import Image
from core.database_containers.abs_database_container import AbstractDatabaseContainer, DatabaseConnectionOpts
from factories.container_factory import ContainerFactory

class RedisImage(Image):
  def __init__(self):
    super().__init__(name="redis", port=6379)


class RedisDatabaseContainer(AbstractDatabaseContainer):
  def __init__(self, name: str, connection_opts: DatabaseConnectionOpts):
    super().__init__(ContainerFactory.InitFromEnv(name, RedisImage()), connection_opts)

  def _connect_command(self, _: DatabaseConnectionOpts) -> str:
    return "redis-cli"

  def _enviroment(self, _: DatabaseConnectionOpts) -> list[str]:
    return []
