# api

The Secure Mailbox API

### Requirements

- [python 3](https://www.python.org/downloads/)
- [pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)
- [docker](https://docs.docker.com/)

### Getting Started

#### Installation

Recommended installation of python and associated packages:

Installing python can be easily done with [pyenv](https://github.com/pyenv/pyenv#installation) (unless you're on windows)

```bash
# To download and install
pyenv install 3.8.1

# To use
pyenv global 3.8.1

# To check
python --version # Python 3.8.1
```

Installing packages and managing virtual environments can be easily done with [pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv):

```bash
# Upgrade pip and setuptools to ensure we can build libraries against 3.8
python -m pip install --upgrade pip setuptools

# Install pipenv and project dependencies
python -m pip install pipenv && pipenv install
```

Other tools used in development:

```bash
# Install the black formatting tool
# Note: Install to global package list
# Docs: https://black.readthedocs.io/en/stable/
python -m pip install --user black
```

### Building and Running

#### Database management

The application uses postgres as it's database backend.

The quickest way to stand up a postgres instance is with docker:

```bash
# Run and daemonize a postgres instance exposing it on 127.0.0.1:5432
# Docs: https://hub.docker.com/_/postgres/
docker run -dp "5432:5432" -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=securemailbox postgres:latest
export DATABASE_URL=postgres://postgres:postgres@127.0.0.1:5432/securemailbox
```

#### Developing on Bare Metal

```bash
# Point flask to run the securemailbox app in development mode
export FLASK_APP=securemailbox FLASK_ENV=development

# Set host to 0.0.0.0 so it can be accessed on the network
pipenv run flask run --host 0.0.0.0 --port 8080
```

#### Building with Docker

```bash
# Build the container setting ENV vars if needed
docker build -t securemailbox/api:latest .

# Run container in interactive mode
docker run -it --network host -e DATABASE_URL=$DATABASE_URL securemailbox/api
```

### Testing

TBD

### Formatting

This repository uses [black](https://github.com/psf/black) to format its files. You can read more about it [here](https://black.readthedocs.io/en/stable/)

To run black on the project:

```bash
# To check which files would be updated
black --check . securemailbox

# To run black on the whole repo
black . securemailbox
```
