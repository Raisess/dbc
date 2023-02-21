#! /usr/bin/env python3

from yacli import CLI

from commands.connect_command import ConnectCommand
from commands.create_command import CreateCommand
from commands.destroy_command import DestroyCommand
from commands.enter_command import EnterCommand
from commands.start_command import StartCommand
from commands.stop_command import StopCommand

if __name__ == "__main__":
  cli = CLI("dbc", [
    CreateCommand(),
    ConnectCommand(),
    EnterCommand(),
    StartCommand(),
    StopCommand(),
    DestroyCommand()
  ])
  cli.handle()
