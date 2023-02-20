# Database Container

Setup development database enviroments with a easy to use database container management tool.

## Supported databases

- [x] MySQL: `mysql`
- [x] PostgreSQL: `postgres`
- [x] MongoDB: `mongo`
- [x] Microsoft SQLServer: `mssql`
- [x] Redis: `redis`

## Supported container managers

- [x] Docker: `docker`
- [x] Podman: `podman`

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
$ dbc create `database-type` `container-name`
```

- NOTE: You can use environment variables to set things like password, check how [here](#environment-variables).

#### `connect`:

Enter into the container using a client software, e.g.: `psql`.

```shell
$ dbc connect `database-type` `container-name`
```

- NOTE: You don't need to specify the environment variables to connect using the `connect` command.

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

## Container managers

By default `dbc` will use `docker`, to use another container set the `CONTAINER` environment variable.

E.g.:

```shell
$ CONTAINER=podman dbc enter `container-name`
```

### Environment variables

**CONTAINER**: Specifies the container manager will want to use.

- Default: `docker`

**DB_NAME**: The database name.

- Default: `mydatabase`

**DB_PORT**: The physical port to access the database trough the container.

- Default: `1234`
- NOTE: Inside the container, the databases will always use they default port, like: `5432` for `postgres`.

**DB_USER**: The username to access the database.

- Default: `root`

**DB_PASS**: The database password.

- Default: `mysecretpassword`
