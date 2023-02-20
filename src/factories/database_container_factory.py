from core.database_containers.abs_database_container import AbstractDatabaseContainer
from core.database_containers.mongo_database_container import MongoDatabaseContainer
from core.database_containers.mysql_database_container import MySqlDatabaseContainer
from core.database_containers.postgres_database_container import PostgresDatabaseContainer
from core.database_containers.redis_database_container import RedisDatabaseContainer
from core.database_containers.sql_server_database_container import SqlServerDatabaseContainer

class DatabaseContinerType:
  Mongo = "mongo"
  MsSql = "mssql"
  MySql = "mysql"
  Postgres = "postgres"
  Redis = "redis"


class DatabaseContainerFactory:
  @staticmethod
  def Init(
    database_type: DatabaseContinerType,
    container_name: str,
  ) -> AbstractDatabaseContainer:
    if database_type == DatabaseContinerType.Postgres:
      return PostgresDatabaseContainer(container_name)
    if database_type == DatabaseContinerType.Mongo:
      return MongoDatabaseContainer(container_name)
    if database_type == DatabaseContinerType.MsSql:
      return SqlServerDatabaseContainer(container_name)
    if database_type == DatabaseContinerType.MySql:
      return MySqlDatabaseContainer(container_name)
    if database_type == DatabaseContinerType.Redis:
      return RedisDatabaseContainer(container_name)
    else:
      raise Exception("Invalid database container type")
