import os
import subprocess

class Shell:
  @staticmethod
  def Execute(command: str) -> str:
    (status, stdout) = subprocess.getstatusoutput(command)
    if status != 0:
      raise Exception(f"Error running command: {command}\n\n{stdout}")

    return stdout

  @staticmethod
  def ExecuteTTY(command: str) -> None:
    os.system(command)
