import os

from core.containers.abs_container import AbstractContainer

class DockerContainer(AbstractContainer):
  def __init__(self, name: str, instance: str, instace_port: int):
    super().__init__(name, instance, instace_port)

  def create(self, env: list[str]) -> None:
    credentials = " ".join(["-e " + credential.strip() for credential in env])
    os.system(f"docker pull {self.get_instance()}")
    os.system(f"docker run --name {self.get_name()} {credentials} --detach -p {self.get_port()}:{self.get_instance_port()} -d {self.get_instance()}")

  def execute(self, command: str) -> None:
    os.system(f"docker exec -it {self.get_name()} {command}")

  def bash(self) -> None:
    self.execute("bash")

  def destroy(self) -> None:
    os.system(f"docker stop {self.get_name()}")
    os.system(f"docker rm {self.get_name()}")
