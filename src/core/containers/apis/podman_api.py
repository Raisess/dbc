import json
import subprocess

class PodmanAPI:
  @staticmethod
  def Pull(image: str) -> None:
    subprocess.getoutput(f"podman pull docker.io/library/{image}")

  @staticmethod
  def Run(container: str, image: str, public_port: int, port: int, env: str = "") -> None:
    subprocess.getoutput(f"podman run --name {container} {env} --detach --publish {public_port}:{port}/tcp docker.io/library/{image}")

  @staticmethod
  def Start(container: str) -> None:
    subprocess.getoutput(f"podman start {container}")

  @staticmethod
  def Stop(container: str) -> None:
    subprocess.getoutput(f"podman stop {container}")

  @staticmethod
  def Eval(container: str, command: str) -> None:
    subprocess.getoutput(f"podman exec -it {container} {command}")

  @staticmethod
  def Delete(container: str) -> None:
    subprocess.getoutput(f"podman rm {container}")

  @staticmethod
  def DeleteVolume(volume: str) -> None:
    subprocess.getoutput(f"podman volume rm {volume}")

  @staticmethod
  def Dump(container: str) -> dict:
    stdout = subprocess.getoutput(f"podman container inspect {container}")
    return json.loads(stdout)[0]
