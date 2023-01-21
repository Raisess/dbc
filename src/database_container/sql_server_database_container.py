from container.docker_container import DockerContainer
from database_container.abs_database_container import AbstractDatabaseContainer, DatabaseConnectionOpts

class SqlServerDatabaseContainer(AbstractDatabaseContainer):
  def __init__(self, name: str, connection_opts: DatabaseConnectionOpts):
    super().__init__(DockerContainer(name, connection_opts.port, "mcr.microsoft.com/mssql/server"), connection_opts)

  def _connect_command(self, connection_opts: DatabaseConnectionOpts) -> str:
    return f"/opt/mssql-tools/bin/sqlcmd -S {connection_opts.host} -U {connection_opts.user} -P {connection_opts.password}"

  def _enviroment(self, connection_opts: DatabaseConnectionOpts) -> list[str]:
    return [
      "ACCEPT_EULA=Y",
      f"MSSQL_SA_PASSWORD={connection_opts.password}"
    ]
