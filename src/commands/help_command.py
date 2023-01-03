from commands.abs_command import AbstractCommand

class HelpCommand(AbstractCommand):
  def __init__(self):
    super().__init__(
      "help",
      "Help command."
    )
    self.__commands = []

  def attach_commands(self, commands: list[AbstractCommand]) -> None:
    self.__commands = commands

  def handle(self, _: list[str]) -> None:
    print("DBC CLI")
    for command in self.__commands:
      print(f"\t {command.get_command()}: {command.get_description()}")
    print("Thanks for using @ Raisess")
