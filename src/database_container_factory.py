from database_container.abs_database_container import AbstractDatabaseServerContainer, DatabaseConnectionOpts
from database_container.mysql_database_container import MySqlServerContainer

class DatabaseContinerType:
  MySql = "mysql"


class DatabaseContainerFactory:
  @staticmethod
  def Init(
    container_name: str,
    database_type: DatabaseContinerType,
    database_connection_opts: DatabaseConnectionOpts | None
  ) -> AbstractDatabaseServerContainer:
    if database_type == DatabaseContinerType.MySql:
      return MySqlServerContainer(container_name, database_connection_opts)
    else:
      raise Exception("Invalid database container type")
