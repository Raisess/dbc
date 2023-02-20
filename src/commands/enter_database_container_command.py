from yacli import Command

from core.containers.abs_container import Image
from factories.container_factory import ContainerFactory
from factories.database_container_factory import DatabaseContainerFactory

class EnterDatabaseContainerCommand(Command):
  def __init__(self):
    super().__init__(
      "enter",
      "Enter the container using `bash` command, e.g.: dbc enter container-name",
      args_len=1
    )

  def handle(self, args: list[str]) -> None:
    container_name = args[0]
    container = ContainerFactory.InitFromEnv(container_name, Image("NULL", 1))
    container.execute("bash")
