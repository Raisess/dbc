import json
import os
import subprocess

from core.containers.abs_container import AbstractContainer, Image

class PodmanContainer(AbstractContainer):
  def __init__(self, name: str, image: Image):
    super().__init__(name, image)

  def create(self, env: list[str]) -> None:
    os.system(f"podman pull docker.io/library/{self.get_image()}")
    os.system(f"podman run --name {self.get_name()} {self._parse_env(env)} --detach --publish {self.get_port()}:{self.get_image_port()}/tcp docker.io/library/{self.get_image()}")

  def execute(self, command: str) -> None:
    os.system(f"podman exec -it {self.get_name()} {command}")

  def destroy(self) -> None:
    volume = self.__get_volume_name()
    if not volume:
      raise Exception("Volume not found for this container")

    os.system(f"podman stop {self.get_name()}")
    os.system(f"podman rm {self.get_name()}")
    os.system(f"podman volume rm {volume}")

  def dump(self) -> dict:
    stdout = subprocess.getoutput(f"podman container inspect {self.get_name()}")
    return json.loads(stdout)[0]

  def __get_volume_name(self) -> str | None:
    mounts: list[dict] | None = self.dump().get("Mounts")
    if not mounts:
      return None
    return mounts[0].get("Name")
