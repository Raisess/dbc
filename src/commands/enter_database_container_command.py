from yacli import Command

from core.database_containers.abs_database_container import DatabaseConnectionOpts
from factories.database_container_factory import DatabaseContainerFactory

class EnterDatabaseContainerCommand(Command):
  def __init__(self):
    super().__init__(
      "enter",
      "Enter the container using `bash` command, e.g.: dbc enter mysql container-name",
      args_len=2
    )

  def handle(self, args: list[str]) -> None:
    database_type = args[0]
    container_name = args[1]
    database_container = DatabaseContainerFactory.Init(container_name, database_type, DatabaseConnectionOpts())
    database_container.enter()
