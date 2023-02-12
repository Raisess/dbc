from core.containers.docker_container import DockerContainer
from core.database_containers.abs_database_container import AbstractDatabaseContainer, DatabaseConnectionOpts

REDIS_CONTAINER_IMAGE = "redis"
REDIS_CONTAINER_PORT = 6379

class RedisDatabaseContainer(AbstractDatabaseContainer):
  def __init__(self, name: str, connection_opts: DatabaseConnectionOpts):
    container = DockerContainer(name, REDIS_CONTAINER_IMAGE, REDIS_CONTAINER_PORT)
    container.bind(connection_opts.port)
    super().__init__(container, connection_opts)

  def _connect_command(self, opts: DatabaseConnectionOpts) -> str:
    return "redis-cli"

  def _enviroment(self, opts: DatabaseConnectionOpts) -> list[str]:
    return []
