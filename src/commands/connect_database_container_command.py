from yacli import Command

from database_container.abs_database_container import DatabaseConnectionOpts
from database_container.database_container_factory import DatabaseContainerFactory

class ConnectDatabaseContainerCommand(Command):
  def __init__(self):
    super().__init__(
      command="connect",
      description="Connect into a database container. E.g.: dbc connect mysql container-name.",
      args_len=2
    )

  def handle(self, args: list[str]) -> None:
    database_type = args[0]
    container_name = args[1]
    container = DatabaseContainerFactory.Init(container_name, database_type, DatabaseConnectionOpts())
    container.connect()