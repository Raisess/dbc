# Database Container

Setup development database enviroments with a easy to use database container management tool.

## Supported databases

- [x] MySQL: `mysql`
- [x] PostgreSQL: `postgres`
- [x] MongoDB: `mongo`
- [x] Microsoft SQLServer: `mssql`
- [x] Redis: `redis`

## Dependencies

- [Python 3.10.x >=](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [yacli](https://github.com/Raisess/yacli) (auto downloaded by the `install.py` script)

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

Create a new container and download a new database image if don't have one.

```shell
$ DB_NAME=database DB_HOST=localhost DB_PORT=3306 DB_USER=root DB_PASS=root dbc create `database-type` `container-name`
```

- @NOTE: needs database env vars.

#### `connect`:

Enter into the container using a client software, e.g.: `psql`.

```shell
$ DB_NAME=database DB_HOST=localhost DB_PORT=3306 DB_USER=root DB_PASS=root dbc connect `database-type` `container-name`
```

- @NOTE: needs database env vars.

#### `enter`:

Enter into the container using `bash`.

```shell
$ dbc enter `container-name`
```

#### `destroy`:

Delete the container and the volume, but keeps the database image.

```shell
$ dbc destroy `container-name`
```
