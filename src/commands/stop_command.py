from yacli import Command

from core.containers.abs_container import Image
from factories.container_factory import ContainerFactory
from factories.database_container_factory import DatabaseContainerFactory

class StopCommand(Command):
  def __init__(self):
    super().__init__(
      "stop",
      "Stop the container, e.g.: dbc stop container-name",
      args_len=1
    )

  def handle(self, args: list[str]) -> None:
    container_name = args[0]
    container = ContainerFactory.InitFromEnv(container_name, Image("NULL", 1))
    container.stop()
    print(f"Successfully stopped container: {container_name}")
