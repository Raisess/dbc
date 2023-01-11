from container.docker_container import DockerContainer
from database_container.abs_database_container import AbstractDatabaseContainer, DatabaseConnectionOpts

class PostgresDatabaseContainer(AbstractDatabaseContainer):
  def __init__(self, name: str, connection_opts: DatabaseConnectionOpts):
    super().__init__(
      DockerContainer(name, "postgres"),
      connection_opts
    )

  def _connect_command(self, connection_opts: DatabaseConnectionOpts) -> str:
    return f"psql -h {connection_opts.host} -U {connection_opts.user} {connection_opts.database}"

  def _enviroment(self, connection_opts: DatabaseConnectionOpts) -> list[str]:
    return [
      f"POSTGRES_DB={connection_opts.database}",
      f"POSTGRES_PASSWORD={connection_opts.password}"
    ]
