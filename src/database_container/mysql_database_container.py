from container.docker_container import DockerContainer
from database_container.abs_database_container import AbstractDatabaseServerContainer, DatabaseConnectionOpts

class DefaultMySqlConnectionOpts(DatabaseConnectionOpts):
  def __init__(self, database: str):
    super().__init__(database, "localhost", "root", "root", 3306)


class MySqlServerContainer(AbstractDatabaseServerContainer):
  def __init__(self, name: str, connection_opts: DatabaseConnectionOpts | None):
    super().__init__(
      DockerContainer(name, "mysql"),
      connection_opts or DefaultMySqlConnectionOpts(name)
    )

  def _connect_command(self, connection_opts: DatabaseConnectionOpts) -> str:
    return f"mysql -u {connection_opts.user} -p {connection_opts.database} --password={connection_opts.password}"

  def _enviroment(self, connection_opts: DatabaseConnectionOpts) -> list[str]:
    return [
      f"MYSQL_DATABASE={connection_opts.database}",
      f"MYSQL_ROOT_PASSWORD={connection_opts.password}"
    ]
