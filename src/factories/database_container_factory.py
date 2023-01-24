from core.database_containers.abs_database_container import AbstractDatabaseContainer, DatabaseConnectionOpts
from core.database_containers.mongo_database_container import MongoDatabaseContainer
from core.database_containers.mysql_database_container import MySqlDatabaseContainer
from core.database_containers.postgres_database_container import PostgresDatabaseContainer
from core.database_containers.sql_server_database_container import SqlServerDatabaseContainer

class DatabaseContinerType:
  MySql = "mysql"
  Postgres = "postgres"
  Mongo = "mongo"
  MsSql = "mssql"


class DatabaseContainerFactory:
  @staticmethod
  def Init(
    container_name: str,
    database_type: DatabaseContinerType,
    database_connection_opts: DatabaseConnectionOpts
  ) -> AbstractDatabaseContainer:
    if database_type == DatabaseContinerType.MySql:
      return MySqlDatabaseContainer(container_name, database_connection_opts)
    if database_type == DatabaseContinerType.Postgres:
      return PostgresDatabaseContainer(container_name, database_connection_opts)
    if database_type == DatabaseContinerType.Mongo:
      return MongoDatabaseContainer(container_name, database_connection_opts)
    if database_type == DatabaseContinerType.MsSql:
      return SqlServerDatabaseContainer(container_name, database_connection_opts)
    else:
      raise Exception("Invalid database container type")
