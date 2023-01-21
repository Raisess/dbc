from container.docker_container import DockerContainer
from database_container.abs_database_container import AbstractDatabaseContainer, DatabaseConnectionOpts

class MongoDatabaseContainer(AbstractDatabaseContainer):
  def __init__(self, name: str, connection_opts: DatabaseConnectionOpts):
    super().__init__(DockerContainer(name, "mongo"), connection_opts)

  def _connect_command(self, connection_opts: DatabaseConnectionOpts) -> str:
    return f"mongosh --host {connection_opts.host} --username {connection_opts.user} --password {connection_opts.password}"

  def _enviroment(self, connection_opts: DatabaseConnectionOpts) -> list[str]:
    return [
      f"MONGO_INITDB_DATABASE={connection_opts.database}",
      f"MONGO_INITDB_ROOT_USERNAME={connection_opts.user}",
      f"MONGO_INITDB_ROOT_PASSWORD={connection_opts.password}"
    ]
