from yacli import Command

from core.containers.docker_container import DockerContainer, Image
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
    container = DockerContainer(container_name, Image("NULL", 1))
    container.execute("bash")
