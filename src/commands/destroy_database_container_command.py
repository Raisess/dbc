from yacli import Command

from core.containers.docker_container import DockerContainer
from factories.database_container_factory import DatabaseContainerFactory

class DestroyDatabaseContainerCommand(Command):
  def __init__(self):
    super().__init__(
      "destroy",
      "Destroy the container (irreversible) command, e.g.: dbc destroy container-nane",
      args_len=1
    )

  def handle(self, args: list[str]) -> None:
    container_name = args[0]
    container = DockerContainer(container_name, "NULL", 1)
    container.destroy()
