class AbstractCommand:
  def __init__(self, command: str, description: str):
    self.__command = command
    self.__description = description

  def get_command(self) -> str:
    return self.__command

  def get_description(self) -> str:
    return self.__description

  def validate_args_len(self, args: list[str], min_len: int) -> None:
    if len(args) < min_len:
      raise Exception("Invalid arguments, try `dbc help`")

  def handle(self, args: list[str]) -> None:
    raise NotImplemented()
