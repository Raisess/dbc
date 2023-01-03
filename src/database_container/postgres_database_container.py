from container.docker_container import DockerContainer
from database_container.abs_database_container import AbstractDatabaseServerContainer, DatabaseConnectionOpts

class DefaultPostgresConnectionOpts(DatabaseConnectionOpts):
  def __init__(self, database: str):
    super().__init__(database, "localhost", "postgres", "postgres", 5432)

class PosgresServerContainer(AbstractDatabaseServerContainer):
  def __init__(self, name: str, connection_opts: DatabaseConnectionOpts | None):
    super().__init__(
      DockerContainer(name, "postgres"),
      connection_opts or DefaultPostgresConnectionOpts(name)
    )

  def _connect_command(self, connection_opts: DatabaseConnectionOpts) -> str:
    return f"psql -h {connection_opts.host} -U {connection_opts.user} {connection_opts.database}"

  def _enviroment(self, connection_opts: DatabaseConnectionOpts) -> list[str]:
    return [
      f"POSTGRES_DB={connection_opts.database}",
      f"POSTGRES_PASSWORD={connection_opts.password}"
    ]
