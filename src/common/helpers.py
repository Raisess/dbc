import subprocess

# Executes a command and return the stdout if the exit status is equal to 0
def execute(command: str) -> str:
  (status, stdout) = subprocess.getstatusoutput(command)
  if status != 0:
    raise Exception(f"Error running command: {command}\n\n{stdout}")

  return stdout
