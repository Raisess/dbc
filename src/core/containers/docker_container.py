import json
import subprocess

from core.containers.abs_container import AbstractContainer, Image

class DockerContainer(AbstractContainer):
  def __init__(self, name: str, image: Image):
    super().__init__(name, image)

  def create(self, env: list[str]) -> None:
    self.__run(f"pull {self.get_image()}")
    self.__run(f"run --name {self.get_name()} {self.__parse_env(env)} --detach -p {self.get_port()}:{self.get_image_port()} -d {self.get_image()}")

  def start(self) -> None:
    self.__run(f"start {self.get_name()}")

  def stop(self) -> None:
    self.__run(f"stop {self.get_name()}")

  def execute(self, command: str) -> None:
    self.__run(f"exec -it {self.get_name()} {command}")

  def destroy(self) -> None:
    volume = self.__get_volume_name()
    if not volume:
      raise Exception("Volume not found for this container")

    self.stop()
    self.__run(f"rm {self.get_name()}")
    self.__run(f"volume rm {volume}")

  def __run(self, command: str) -> str:
    return subprocess.getoutput(f"docker {command}")

  def __parse_env(self, env: list[str]) -> str:
    return " ".join(["-e " + credential.strip() for credential in env])

  def __get_volume_name(self) -> str | None:
    stdout = self.__run(f"container inspect {self.get_name()}")
    dump = json.loads(stdout)[0]

    mounts: list[dict] | None = dump.get("Mounts")
    if not mounts:
      return None
    return mounts[0].get("Name")
