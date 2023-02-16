from core.containers.docker_container import DockerContainer, Image
from core.database_containers.abs_database_container import AbstractDatabaseContainer, DatabaseConnectionOpts

class MySqlImage(Image):
  def __init__(self):
    super().__init__(name="mysql", port=3306)


class MySqlDatabaseContainer(AbstractDatabaseContainer):
  def __init__(self, name: str, connection_opts: DatabaseConnectionOpts):
    super().__init__(DockerContainer(name, MySqlImage()), connection_opts)

  def _connect_command(self, connection_opts: DatabaseConnectionOpts) -> str:
    return f"mysql --user={connection_opts.user} --database={connection_opts.database} --password={connection_opts.password}"

  def _enviroment(self, connection_opts: DatabaseConnectionOpts) -> list[str]:
    return [
      f"MYSQL_DATABASE={connection_opts.database}",
      f"MYSQL_ROOT_PASSWORD={connection_opts.password}"
    ]
