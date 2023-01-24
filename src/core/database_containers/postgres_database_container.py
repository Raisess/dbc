from core.containers.docker_container import DockerContainer
from core.database_containers.abs_database_container import AbstractDatabaseContainer, DatabaseConnectionOpts

POSTGRES_CONTAINER_INSTANCE = "postgres"
POSTGRES_CONTAINER_PORT = 5432

class PostgresDatabaseContainer(AbstractDatabaseContainer):
  def __init__(self, name: str, connection_opts: DatabaseConnectionOpts):
    container = DockerContainer(name, POSTGRES_CONTAINER_INSTANCE, POSTGRES_CONTAINER_PORT)
    container.bind(connection_opts.port)
    super().__init__(container, connection_opts)

  def _connect_command(self, connection_opts: DatabaseConnectionOpts) -> str:
    return f"psql -h {connection_opts.host} -U {connection_opts.user} {connection_opts.database}"

  def _enviroment(self, connection_opts: DatabaseConnectionOpts) -> list[str]:
    return [
      f"POSTGRES_DB={connection_opts.database}",
      f"POSTGRES_PASSWORD={connection_opts.password}"
    ]