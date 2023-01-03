from commands.abs_command import AbstractCommand
from database_container.database_container_factory import DatabaseContainerFactory

class ConnectDatabaseContainerCommand(AbstractCommand):
  def __init__(self):
    super().__init__(
      "connect",
      "Connect into a database container. E.g.: dbc connect mysql container-name."
    )

  def handle(self, args: list[str]) -> None:
    self.validate_args_len(args, 2)

    database_type = args[0]
    container_name = args[1]
    container = DatabaseContainerFactory.Init(container_name, database_type, None)
    container.connect()
