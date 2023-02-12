from core.containers.docker_container import DockerContainer
from core.database_containers.abs_database_container import AbstractDatabaseContainer, DatabaseConnectionOpts

SQL_SERVER_CONTAINER_IMAGE = "mcr.microsoft.com/mssql/server"
SQL_SERVER_CONTAINER_PORT = 1433

class SqlServerDatabaseContainer(AbstractDatabaseContainer):
  def __init__(self, name: str, connection_opts: DatabaseConnectionOpts):
    container = DockerContainer(name, SQL_SERVER_CONTAINER_IMAGE, SQL_SERVER_CONTAINER_PORT)
    container.bind(connection_opts.port)
    super().__init__(container, connection_opts)

  def _connect_command(self, connection_opts: DatabaseConnectionOpts) -> str:
    return f"/opt/mssql-tools/bin/sqlcmd -S {connection_opts.host} -U {connection_opts.user} -P {connection_opts.password}"

  def _enviroment(self, connection_opts: DatabaseConnectionOpts) -> list[str]:
    return [
      "ACCEPT_EULA=Y",
      f"MSSQL_SA_PASSWORD={connection_opts.password}"
    ]
