from yacli import Command

from database_containers.abs_database_container import DatabaseConnectionOpts
from factories.database_container_factory import DatabaseContainerFactory

class CreateDatabaseContainerCommand(Command):
  def __init__(self):
    super().__init__(
      command="create",
      description="Create a new database container. E.g.: dbc create mysql container-name.",
      args_len=2
    )

  def handle(self, args: list[str]) -> None:
    database_type = args[0]
    container_name = args[1]
    container = DatabaseContainerFactory.Init(container_name, database_type, DatabaseConnectionOpts())
    container.create()
