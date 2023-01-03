#! /usr/bin/env python3

import os
import sys

from commands.connect_database_container_command import ConnectDatabaseContainerCommand
from commands.create_database_container_command import CreateDatabaseContainerCommand
from commands.help_command import HelpCommand

class InvalidCommandException(Exception):
  def __init__(self):
    super().__init__("Invalid command, try `dbc help`")


command_handlers = [
  HelpCommand(),
  CreateDatabaseContainerCommand(),
  ConnectDatabaseContainerCommand(),
]

if __name__ == "__main__":
  if len(sys.argv) < 2:
    raise InvalidCommandException()

  command_handlers[0].attach_commands(command_handlers)

  executed = False
  command = sys.argv[1]
  for command_handler in command_handlers:
    if command_handler.get_command() == command:
      executed = True
      command_handler.handle(sys.argv[2:])

  if not executed:
    raise InvalidCommandException()
