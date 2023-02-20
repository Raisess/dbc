from yacli import Command

from core.containers.abs_container import Image
from factories.container_factory import ContainerFactory
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
    container = ContainerFactory.InitFromEnv(container_name, Image("NULL", 1))
    container.destroy()
