from core.containers.abs_container import Image
from core.database_containers.abs_database_container import AbstractDatabaseContainer, DatabaseConnectionOpts
from factories.container_factory import ContainerFactory

class MsSqlImage(Image):
  def __init__(self):
    super().__init__(name="mcr.microsoft.com/mssql/server", port=1433)


class SqlServerDatabaseContainer(AbstractDatabaseContainer):
  def __init__(self, name: str):
    super().__init__(ContainerFactory.InitFromEnv(name, MsSqlImage()))

  def _connect_command(self, connection_opts: DatabaseConnectionOpts) -> str:
    return f"/opt/mssql-tools/bin/sqlcmd -S {connection_opts.host} -U {connection_opts.user} -P {connection_opts.password}"

  def _enviroment(self, connection_opts: DatabaseConnectionOpts) -> list[str]:
    return [
      "ACCEPT_EULA=Y",
      f"MSSQL_SA_PASSWORD={connection_opts.password}"
    ]
