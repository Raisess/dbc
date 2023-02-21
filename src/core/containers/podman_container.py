from core.containers.apis.podman_api import PodmanAPI
from core.containers.abs_container import AbstractContainer, Image

class PodmanContainer(AbstractContainer):
  def __init__(self, name: str, image: Image):
    super().__init__(name, image)

  def create(self, env: list[str]) -> None:
    PodmanAPI.Pull(self.get_image())
    PodmanAPI.Run(
      container=self.get_name(),
      image=self.get_image(),
      public_port=self.get_port(),
      port=self.get_image_port(),
      env=self.__parse_env(env)
    )

  def start(self) -> None:
    PodmanAPI.Start(self.get_name())

  def stop(self) -> None:
    PodmanAPI.Stop(self.get_name())

  def execute(self, command: str) -> None:
    PodmanAPI.Eval(self.get_name(), command)

  def destroy(self) -> None:
    # Have to get the volume name (ID) before stopping the container
    volume = self.__get_volume_name()
    PodmanAPI.Stop(self.get_name())
    PodmanAPI.Delete(self.get_name())
    if volume:
      PodmanAPI.DeleteVolume(volume)

  def __parse_env(self, env: list[str]) -> str:
    return " ".join(["-e " + credential.strip() for credential in env])

  def __get_volume_name(self) -> str | None:
    dump = PodmanAPI.Dump(self.get_name())
    mounts: list[dict] | None = dump.get("Mounts")
    if not mounts:
      return None
    return mounts[0].get("Name")
