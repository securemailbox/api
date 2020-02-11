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

#### Running on Bare Metal

```bash
# Start flask with hot reload and the debugger
export FLASK_ENV=development

# Set host to 0.0.0.0 so it can be accessed on the network
pipenv run flask run --host 0.0.0.0 --port 8080
```

#### Running in Docker
```bash
# Build the container setting ENV vars if needed
docker build -t securemailbox/api:latest .

# Run container in interactive mode
docker run -it -p 8082:8082 securemailbox/api
```
