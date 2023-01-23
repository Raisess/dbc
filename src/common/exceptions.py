class DatabaseConnectionParamNotProvidedException(Exception):
  def __init__(self, param: str):
    super().__init__(f"Database connection {param} env var not provided")

class ContainerParamNotProvidedException(Exception):
  def __init__(self, param: str):
    super().__init__(f"Container {param} parameter not provided")
