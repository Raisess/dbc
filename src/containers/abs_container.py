class AbstractContainer:
  def __init__(self, name: str, instance: str, instance_port: int):
    if not name:
      raise Exception("Container name not provided")
    if not instance:
      raise Exception("Container instance not provided")
    if not instance_port:
      raise Exception("Container instance port not provided")

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
    self.execute("bash")
