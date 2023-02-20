import os

from core.containers.abs_container import AbstractContainer, Image
from core.containers.docker_container import DockerContainer
from core.containers.podman_container import PodmanContainer

class ContainerType:
  Docker = "docker"
  Podman = "podman"


class ContainerFactory:
  @staticmethod
  def Init(
    container_type: ContainerType,
    container_name: str,
    image: Image
  ) -> AbstractContainer:
    if container_type == ContainerType.Docker:
      return DockerContainer(container_name, image)
    elif container_type == ContainerType.Podman:
      return PodmanContainer(container_name, image)
    else:
      raise Exception("Invalid container type")

  @staticmethod
  def InitFromEnv(name: str, image: Image) -> AbstractContainer:
    container_type = os.getenv("CONTAINER") or ContainerType.Docker
    return ContainerFactory.Init(container_type, name, image)
