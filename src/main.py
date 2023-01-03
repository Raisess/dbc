#! /usr/bin/env python3

import os
import sys

from database_container_factory import DatabaseContainerFactory

if __name__ == "__main__":
  if len(sys.argv) < 2:
    raise Exception("Invalid command, try `dbc help`")

  command = sys.argv[1]
  if command == "create":
    container_name = sys.argv[3]
    database_type = sys.argv[2]
    container = DatabaseContainerFactory.Init(container_name, database_type, None)
    container.create()
  elif command == "connect":
    container_name = sys.argv[3]
    database_type = sys.argv[2]
    container = DatabaseContainerFactory.Init(container_name, database_type, None)
    container.connect()
  elif command == "help":
    print("DBC CLI")
    print("\t create: create's a new database container. E.g.: dbc create mysql container-name")
    print("\t connect: connect's into a database container. E.g.: dbc connect mysql container-name")
    print("Thanks for using @ Raisess")
  else:
    raise Exception("Invalid command")
