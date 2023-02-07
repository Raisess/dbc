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
$ ./install.py
$ dbc help
```

## How to use?

#### `create`:

```shell
$ DB_NAME=database DB_HOST=localhost DB_PORT=3306 DB_USER=root DB_PASS=root dbc create `database-type` `container-name`
```

- @NOTE: needs database env vars.

#### `connect`:

```shell
$ DB_NAME=database DB_HOST=localhost DB_PORT=3306 DB_USER=root DB_PASS=root dbc connect `database-type` `container-name`
```

- @NOTE: needs database env vars.
- @NOTE: connect command, enter a database conntainer using a client software, e.g.: `psql`.

#### `enter`:

```shell
$ dbc enter `container-name`
```

- @NOTE: enter into the container using `bash`.

#### `destroy`:

```shell
$ dbc destroy `container-name`
```
