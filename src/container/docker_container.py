import os

from container.abs_container import AbstractContainer

class DockerContainer(AbstractContainer):
  def __init__(self, name: str, instance: str):
    super().__init__(name, instance)

  def create(self, env: list[str]) -> None:
    credentials = " ".join(["-e " + credential.strip() for credential in env])
    os.system(f"docker run --name {self.get_name()} {credentials} -d {self.get_instance()}")

  def execute(self, command: str) -> None:
    os.system(f"docker exec -it {self.get_name()} {command}")
