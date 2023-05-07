import json

from common.helpers import Shell

class PodmanAPI:
  @staticmethod
  def Pull(image: str) -> None:
    Shell.Execute(f"podman pull docker.io/library/{image}")

  @staticmethod
  def CreateNetwork(label: str) -> None:
    Shell.Execute(f"podman network create {label}")

  @staticmethod
  def Run(container: str, image: str, public_port: int, port: int, env: str = "", net: str = None) -> None:
    if net:
      Shell.Execute(f"podman run --name {container} --net {net} {env} --detach --publish {public_port}:{port}/tcp docker.io/library/{image}")
    else:
      Shell.Execute(f"podman run --name {container} {env} --detach --publish {public_port}:{port}/tcp docker.io/library/{image}")

  @staticmethod
  def Start(container: str) -> None:
    Shell.Execute(f"podman start {container}")

  @staticmethod
  def Stop(container: str) -> None:
    Shell.Execute(f"podman stop {container}")

  @staticmethod
  def Eval(container: str, command: str) -> None:
    Shell.ExecuteTTY(f"podman exec -it {container} {command}")

  @staticmethod
  def Delete(container: str) -> None:
    Shell.Execute(f"podman rm {container}")

  @staticmethod
  def DeleteVolume(volume: str) -> None:
    Shell.Execute(f"podman volume rm {volume}")

  @staticmethod
  def Dump(container: str) -> dict:
    stdout = Shell.Execute(f"podman container inspect {container}")
    return json.loads(stdout)[0]
