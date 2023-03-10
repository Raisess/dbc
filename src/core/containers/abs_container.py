from common.exceptions import ContainerParamNotProvidedException, ImageParamNotProvidedException

class Image:
  def __init__(self, name: str, port: int, version: str = None):
    if not name:
      raise ImageParamNotProvidedException("name")
    if not port:
      raise ImageParamNotProvidedException("port")

    self.name = name
    self.port = port
    if version:
      self.name = f"{name}:{version}"


class AbstractContainer:
  def __init__(self, name: str, image: Image):
    if not name:
      raise ContainerParamNotProvidedException("name")

    self.__name = name
    self.__port = None
    self.__image = image

  def bind(self, port: int) -> None:
    self.__port = port

  def get_name(self) -> str:
    return self.__name

  def get_port(self) -> int:
    if not self.__port:
      raise Exception(f"Port not binded for {self.__name} container")

    return self.__port

  def get_image(self) -> str:
    return self.__image.name

  def get_image_port(self) -> int:
    return self.__image.port

  # Download the image
  # Start the container with the specified env
  def create(self, env: list[str]) -> None:
    raise NotImplemented()

  # Start the container
  def start(self) -> None:
    raise NotImplemented()

  # Stop the container
  def stop(self) -> None:
    raise NotImplemented()

  # Execute a command inside the container
  def execute(self, command: str) -> None:
    raise NotImplemented()

  # Stop the container
  # Delete the container
  # Delete the volume
  def destroy(self) -> None:
    raise NotImplemented()
