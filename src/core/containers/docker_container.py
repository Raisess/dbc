import os

from common.helpers import Shell
from core.containers.abs_container import AbstractContainer, Image

NET = os.getenv("NET")

class DockerContainer(AbstractContainer):
  def __init__(self, name: str, image: Image):
    super().__init__(name, image)

  def create(self, env: list[str]) -> None:
    Shell.Execute(f"docker pull {self.get_image()}")
    if NET:
      Shell.Execute(f"docker network create {NET}")
      Shell.Execute(f"docker run --name {self.get_name()} --net {NET} {self.__parse_env(env)} --detach -p {self.get_port()}:{self.get_image_port()} -d {self.get_image()}")
    else:
      Shell.Execute(f"docker run --name {self.get_name()} {self.__parse_env(env)} --detach -p {self.get_port()}:{self.get_image_port()} -d {self.get_image()}")

  def start(self) -> None:
    Shell.Execute(f"docker start {self.get_name()}")

  def stop(self) -> None:
    Shell.Execute(f"docker stop {self.get_name()}")

  def execute(self, command: str) -> None:
    Shell.ExecuteTTY(f"docker exec -it {self.get_name()} {command}")

  def destroy(self) -> None:
    volume = self.__get_volume_name()
    if not volume:
      raise Exception("Volume not found for this container")

    self.stop()
    Shell.Execute(f"docker rm {self.get_name()}")
    Shell.Execute(f"docker volume rm {volume}")

  def __parse_env(self, env: list[str]) -> str:
    return " ".join(["-e " + credential.strip() for credential in env])

  def __get_volume_name(self) -> str | None:
    import json

    stdout = Shell.Execute(f"docker container inspect {self.get_name()}")
    dump = json.loads(stdout)[0]

    mounts: list[dict] | None = dump.get("Mounts")
    if not mounts:
      return None
    return mounts[0].get("Name")
