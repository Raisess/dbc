from common.exceptions import ContainerParamNotProvidedException

class AbstractContainer:
  def __init__(self, name: str, instance: str, instance_port: int):
    if not name:
      raise ContainerParamNotProvidedException("name")
    if not instance:
      raise ContainerParamNotProvidedException("instance")
    if not instance_port:
      raise ContainerParamNotProvidedException("instance_port")

    self.__name = name
    self.__port = instance_port
    self.__instance = instance
    self.__instance_port = instance_port

  def bind(self, port: int) -> None:
    self.__port = port

  def get_name(self) -> str:
    return self.__name

  def get_port(self) -> int:
    return self.__port

  def get_instance(self) -> str:
    return self.__instance

  def get_instance_port(self) -> int:
    return self.__instance_port

  def create(self, env: list[str]) -> None:
    raise NotImplemented()

  def execute(self, command: str) -> None:
    raise NotImplemented()

  def bash(self) -> None:
    raise NotImplemented()

  def destroy(self) -> None:
    raise NotImplemented()
