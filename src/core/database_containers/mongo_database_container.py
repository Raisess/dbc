from core.containers.docker_container import DockerContainer
from core.database_containers.abs_database_container import AbstractDatabaseContainer, DatabaseConnectionOpts

MONGO_CONTAINER_IMAGE = "mongo"
MONGO_CONTAINER_PORT = 27017

class MongoDatabaseContainer(AbstractDatabaseContainer):
  def __init__(self, name: str, connection_opts: DatabaseConnectionOpts):
    container = DockerContainer(name, MONGO_CONTAINER_IMAGE, MONGO_CONTAINER_PORT)
    container.bind(connection_opts.port)
    super().__init__(container, connection_opts)

  def _connect_command(self, connection_opts: DatabaseConnectionOpts) -> str:
    return f"mongosh --host {connection_opts.host} --username {connection_opts.user} --password {connection_opts.password}"

  def _enviroment(self, connection_opts: DatabaseConnectionOpts) -> list[str]:
    return [
      f"MONGO_INITDB_DATABASE={connection_opts.database}",
      f"MONGO_INITDB_ROOT_USERNAME={connection_opts.user}",
      f"MONGO_INITDB_ROOT_PASSWORD={connection_opts.password}"
    ]
