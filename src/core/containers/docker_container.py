import os

from core.containers.abs_container import AbstractContainer, Image

class DockerContainer(AbstractContainer):
  def __init__(self, name: str, image: Image):
    super().__init__(name, image)

  def create(self, env: list[str]) -> None:
    os.system(f"docker pull {self.get_image()}")
    credentials = " ".join(["-e " + credential.strip() for credential in env])
    os.system(f"docker run --name {self.get_name()} {credentials} --detach -p {self.get_port()}:{self.get_image_port()} -d {self.get_image()}")

  def execute(self, command: str) -> None:
    os.system(f"docker exec -it {self.get_name()} {command}")

  # @TODO: delete the container volume
  def destroy(self) -> None:
    os.system(f"docker stop {self.get_name()}")
    os.system(f"docker rm {self.get_name()}")
