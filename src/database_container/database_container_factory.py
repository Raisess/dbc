from database_container.abs_database_container import AbstractDatabaseContainer, DatabaseConnectionOpts
from database_container.mongo_database_container import MongoDatabaseContainer
from database_container.mysql_database_container import MySqlDatabaseContainer
from database_container.postgres_database_container import PostgresDatabaseContainer
from database_container.sql_server_database_container import SqlServerDatabaseContainer

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
