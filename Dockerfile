FROM python:3-slim as build-env

RUN apt-get update && \
    apt-get upgrade -y && \
    # Required for building psycopg2 from source 
    apt-get install -y libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/

# Install and upgrade pip, setuptools, and pipenv
RUN python -m pip install --upgrade pip setuptools pipenv

# Only copy dependency files so pipenv install layer can be cached
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install

COPY . .
ENV FLASK_ENV "production"
ENV FLASK_APP "securemailbox"

CMD [ "pipenv", "run", "flask", "run", "--port", "8082" ]
