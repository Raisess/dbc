from core.containers.abs_container import Image
from core.database_containers.abs_database_container import AbstractDatabaseContainer, DatabaseConnectionOpts
from factories.container_factory import ContainerFactory

class MongoImage(Image):
  def __init__(self):
    super().__init__(name="mongo", port=27017)


class MongoDatabaseContainer(AbstractDatabaseContainer):
  def __init__(self, name: str, connection_opts: DatabaseConnectionOpts):
    super().__init__(ContainerFactory.InitFromEnv(name, MongoImage()), connection_opts)

  def _connect_command(self, connection_opts: DatabaseConnectionOpts) -> str:
    return f"mongosh --host {connection_opts.host} --username {connection_opts.user} --password {connection_opts.password}"

  def _enviroment(self, connection_opts: DatabaseConnectionOpts) -> list[str]:
    return [
      f"MONGO_INITDB_DATABASE={connection_opts.database}",
      f"MONGO_INITDB_ROOT_USERNAME={connection_opts.user}",
      f"MONGO_INITDB_ROOT_PASSWORD={connection_opts.password}"
    ]
