# api

The Secure Mailbox API

[![Build Status](https://www.travis-ci.org/securemailbox/api.svg?branch=develop)](https://www.travis-ci.org/securemailbox/api)

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

#### Building with docker-compose

The container cluster uses:

    python:3-slim for application code
    postgres:latest for database management
    nginx:latest for reverse proxying requests to/from app container

Default environment variables are in the ```.env``` file.

They specify the

* database
    * user
    * password
    * name
    * host
    * port
* name of the compose cluster
* domain name for setting up SSL/TLS.
* an email for setting up with certbot

Nginx is configured to use default port 80.
It will use port 443 for TLS if you are running the production version.

##### Initialize Database

Before the first run of the cluster, the database needs to be initialized. The easiest way is to startup the db container by itself.

```bash
docker-compose up db -d
```


##### Set up SSL/TLS

To use the TLS version, you must first set up certificates from [Let's Encrypt](https://letsencrypt.org/). If you intend on running locally for development without SSL/TLS you can skip this.

To get a certificate from Let's Encrypt we use the certbot docker container.

First change DOMAIN_NAME and EMAIL in the ```.env``` file to your domain and email.

Next bring up a temporary site for the certbot's challenge to prove you have control over the server at your domain.

```bash
cd letsencrypt/letsencrypt-site
docker-compose up -d
```

Run the certbot container

```bash
docker run -it --rm \
-v ./letsencrypt/etc/letsencrypt:/etc/letsencrypt \
-v ./letsencrypt/var/lib/letsencrypt:/var/lib/letsencrypt \
-v ./letsencrypt/data/letsencrypt:/data/letsencrypt \
-v ./letsencrypt/var/log/letsencrypt:/var/log/letsencrypt \
certbot/certbot \
certonly --webroot \
--email ${EMAIL} --agree-tos --no-eff-email \
--webroot-path=/data/letsencrypt \
-d ${DOMAIN_NAME} -d www.${DOMAIN_NAME}
```
It will place the certs in letsencrypt/etc/letsencrypt that we use in our nginx container.

Bring down the temporary site.

```bash
docker-compose down
```

Next create a Diffie-Hellman parameters file. This will take a while.

```bash
mkdir dh-param
openssl dhparam -out dh-param/dhparam-2048.pem 2048
```


##### Start the cluster

```bash
# Build and run the docker-compose cluster
# without TLS
docker-compose up --build
# With TLS
docker-compose -f docker-compose.production.yml up --build
```


### Testing

Install pytest for our premade tests.
If you installed everything in the pipfile pytest should already be installed.

```bash
pipenv install pytest --dev
```
Make sure the DATABASE_URL is correct, and it can run normally in flask.
This is the testing url:

```bash
export DATABASE_URL=postgres://postgres:postgres@127.0.0.1:5432/test
```
Run with:

```bash
pipenv run pytest
```
This will run created tests with filenames that start with 'test'.

### Formatting

This repository uses [black](https://github.com/psf/black) to format its files. You can read more about it [here](https://black.readthedocs.io/en/stable/)

To run black on the project:

```bash
# To check which files would be updated
black --check . securemailbox

# To run black on the whole repo
black . securemailbox
```
