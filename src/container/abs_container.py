class AbstractContainer:
  def __init__(self, name: str, port: int, instance: str):
    if not name:
      raise Exception("Container name not provided")
    if not port:
      raise Exception("Container port not provided")
    if not instance:
      raise Exception("Container instance not provided")

    self.__name = name
    self.__port = port
    self.__instance = instance

  def get_name(self) -> str:
    return self.__name

  def get_port(self) -> int:
    return self.__port

  def get_instance(self) -> str:
    return self.__instance

  def create(self, env: list[str]) -> None:
    raise NotImplemented()

  def execute(self, command: str) -> None:
    raise NotImplemented()

  def bash(self) -> None:
    self.execute("bash")
