from yacli import Command

from factories.database_container_factory import DatabaseContainerFactory

class CreateCommand(Command):
  def __init__(self):
    super().__init__(
      command="create",
      description="Create a new database container. E.g.: dbc create mysql container-name.",
      args_len=2
    )

  def handle(self, args: list[str]) -> None:
    database_type = args[0]
    container_name = args[1]
    database_container = DatabaseContainerFactory.Init(database_type, container_name)
    print("Preparing stuff, please wait...")
    database_container.create()
    print(f"Successfully created container: {container_name}")
