# Database Container

Setup development database enviroments with a easy to use database container management tool.

## Supported databases

- [x] MySQL: `mysql`
- [x] PostgreSQL: `postgres`
- [x] MongoDB: `mongo`
- [x] Microsoft SQLServer: `mssql`

## Dependencies

- [Python 3.10.x >=](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [yacli](https://github.com/Raisess/yacli)

## Setup

How to download and install:

```shell
$ git clone https://github.com/Raisess/dbc
$ cd dbc
$ sudo ./install.py
$ dbc help
```

## How to use?

#### `create`:

```shell
$ dbc create `database-type` `container-name`
```

#### `connect`:

```shell
$ dbc connect `database-type` `container-name`
```

- NOTE: connect command, enter a database conntainer using a client software, e.g.: `psql`.

#### Example:

- MySQL database container:

```shell
$ DB_NAME=database DB_HOST=localhost DB_PORT=3306 DB_USER=root DB_PASS=root dbc create mysql mysql-container-name
$ DB_NAME=database DB_HOST=localhost DB_PORT=3306 DB_USER=root DB_PASS=root dbc connect mysql mysql-container-name
```
