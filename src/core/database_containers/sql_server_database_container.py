from core.containers.docker_container import DockerContainer, Image
from core.database_containers.abs_database_container import AbstractDatabaseContainer, DatabaseConnectionOpts

class MsSqlImage(Image):
  def __init__(self):
    super().__init__(name="mcr.microsoft.com/mssql/server", port=1433)


class SqlServerDatabaseContainer(AbstractDatabaseContainer):
  def __init__(self, name: str, connection_opts: DatabaseConnectionOpts):
    super().__init__(DockerContainer(name, MsSqlImage()), connection_opts)

  def _connect_command(self, connection_opts: DatabaseConnectionOpts) -> str:
    return f"/opt/mssql-tools/bin/sqlcmd -S {connection_opts.host} -U {connection_opts.user} -P {connection_opts.password}"

  def _enviroment(self, connection_opts: DatabaseConnectionOpts) -> list[str]:
    return [
      "ACCEPT_EULA=Y",
      f"MSSQL_SA_PASSWORD={connection_opts.password}"
    ]
