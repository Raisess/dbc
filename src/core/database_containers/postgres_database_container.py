from core.containers.abs_container import Image
from core.database_containers.abs_database_container import AbstractDatabaseContainer, DatabaseConnectionOpts
from factories.container_factory import ContainerFactory

class PostgresImage(Image):
  def __init__(self):
    super().__init__(name="postgres", port=5432)


class PostgresDatabaseContainer(AbstractDatabaseContainer):
  def __init__(self, name: str, connection_opts: DatabaseConnectionOpts):
    super().__init__(ContainerFactory.InitFromEnv(name, PostgresImage()), connection_opts)

  def _connect_command(self, connection_opts: DatabaseConnectionOpts) -> str:
    return f"psql -h {connection_opts.host} -U {connection_opts.user} {connection_opts.database}"

  def _enviroment(self, connection_opts: DatabaseConnectionOpts) -> list[str]:
    return [
      f"POSTGRES_DB={connection_opts.database}",
      f"POSTGRES_PASSWORD={connection_opts.password}"
    ]
