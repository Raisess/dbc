import json
import os
import subprocess

from core.containers.abs_container import AbstractContainer, Image

class DockerContainer(AbstractContainer):
  def __init__(self, name: str, image: Image):
    super().__init__(name, image)

  def create(self, env: list[str]) -> None:
    os.system(f"docker pull {self.get_image()}")
    os.system(f"docker run --name {self.get_name()} {self._parse_env(env)} --detach -p {self.get_port()}:{self.get_image_port()} -d {self.get_image()}")

  def execute(self, command: str) -> None:
    os.system(f"docker exec -it {self.get_name()} {command}")

  def destroy(self) -> None:
    volume = self.__get_volume_name()
    if not volume:
      raise Exception("Volume not found for this container")

    os.system(f"docker stop {self.get_name()}")
    os.system(f"docker rm {self.get_name()}")
    os.system(f"docker volume rm {volume}")

  def dump(self) -> dict:
    stdout = subprocess.getoutput(f"docker container inspect {self.get_name()}")
    return json.loads(stdout)[0]

  def __get_volume_name(self) -> str | None:
    mounts: list[dict] | None = self.dump().get("Mounts")
    if not mounts:
      return None
    return mounts[0].get("Name")
