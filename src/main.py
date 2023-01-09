#! /usr/bin/env python3

from yacli import CLI

from commands.connect_database_container_command import ConnectDatabaseContainerCommand
from commands.create_database_container_command import CreateDatabaseContainerCommand

if __name__ == "__main__":
  cli = CLI("dbc", [ConnectDatabaseContainerCommand(), CreateDatabaseContainerCommand()])
  cli.handle()
