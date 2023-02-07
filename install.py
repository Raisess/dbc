#! /usr/bin/env python3

import os
import site

CLI_NAME = "dbc"

BIN_PATH = f"/usr/local/bin/{CLI_NAME}"
LIB_PATH = f"/usr/local/lib/{CLI_NAME}"
ETC_PATH = f"/usr/local/etc/{CLI_NAME}"

if __name__ == "__main__":
  print(f"Installing {CLI_NAME}...")

  if not os.path.isdir(f"{site.USER_SITE}/yacli"):
    os.system("""
      git clone https://github.com/Raisess/yacli
      cd yacli
      ./install.sh
      cd ..
      rm -rf yacli
    """)

  if os.path.isfile("./requirements.txt"):
    os.system("python3 -m pip install -r ./requirements.txt")

  if os.path.isdir(BIN_PATH):
    os.system(f"sudo rm -rf {BIN_PATH}")
  os.system(f"sudo cp ./bin/{CLI_NAME} {BIN_PATH}")

  if os.path.isdir(LIB_PATH):
    os.system(f"sudo rm -rf {LIB_PATH}")
  os.system(f"sudo cp -r ./src {LIB_PATH}")

  if os.path.isdir("./etc"):
    if os.path.isdir(ETC_PATH):
      os.system(f"sudo rm -rf {ETC_PATH}")
    os.system(f"sudo cp -r ./etc {ETC_PATH}")

  print("Installed successfully!")