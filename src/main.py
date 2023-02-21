#! /usr/bin/env python3

from yacli import CLI

from commands.connect_command import ConnectCommand
from commands.create_command import CreateCommand
from commands.destroy_command import DestroyCommand
from commands.enter_command import EnterCommand

if __name__ == "__main__":
  cli = CLI("dbc", [
    CreateCommand(),
    ConnectCommand(),
    EnterCommand(),
    DestroyCommand()
  ])
  cli.handle()
