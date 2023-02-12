from common.exceptions import ContainerParamNotProvidedException

class AbstractContainer:
  def __init__(self, name: str, image: str, image_port: int):
    if not name:
      raise ContainerParamNotProvidedException("name")
    if not image:
      raise ContainerParamNotProvidedException("image")
    if not image_port:
      raise ContainerParamNotProvidedException("image_port")

    self.__name = name
    self.__port = image_port
    self.__image = image
    self.__image_port = image_port

  def bind(self, port: int) -> None:
    self.__port = port

  def get_name(self) -> str:
    return self.__name

  def get_port(self) -> int:
    return self.__port

  def get_image(self) -> str:
    return self.__image

  def get_image_port(self) -> int:
    return self.__image_port

  def create(self, env: list[str]) -> None:
    raise NotImplemented()

  def execute(self, command: str) -> None:
    raise NotImplemented()

  def bash(self) -> None:
    raise NotImplemented()

  def destroy(self) -> None:
    raise NotImplemented()
