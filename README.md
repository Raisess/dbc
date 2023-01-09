# Database Container

Setup development database enviroments with a easy to use database container management tool.

## Supported databases

- [x] MySQL
- [x] PostgreSQL
- [ ] MongoDB

## Dependencies

- [Python 3.10.x >=](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [yacli](https://github.com/Raisess/yacli)

## Setup

How to download and install:

```shell
$ git clone https://github.com/Raisess/dbc
$ cd dbc
$ ./install.sh
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
$ dbc create mysql mysql-container-name
$ dbc connect mysql mysql-container-name
```
