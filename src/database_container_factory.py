from database_container.abs_database_container import AbstractDatabaseServerContainer, DatabaseConnectionOpts
from database_container.mysql_database_container import MySqlServerContainer
from database_container.postgres_database_container import PosgresServerContainer

class DatabaseContinerType:
  MySql = "mysql"
  Postgres = "postgres"


class DatabaseContainerFactory:
  @staticmethod
  def Init(
    container_name: str,
    database_type: DatabaseContinerType,
    database_connection_opts: DatabaseConnectionOpts | None
  ) -> AbstractDatabaseServerContainer:
    if database_type == DatabaseContinerType.MySql:
      return MySqlServerContainer(container_name, database_connection_opts)
    if database_type == DatabaseContinerType.Postgres:
      return PosgresServerContainer(container_name, database_connection_opts)
    else:
      raise Exception("Invalid database container type")
