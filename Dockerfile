FROM python:3-slim

COPY . .

RUN python -m pip install --upgrade pip setuptools && python -m pip install pipenv
RUN pipenv install

ENV FLASK_ENV "production"

CMD [ "pipenv", "run", "flask", "run", "--port", "8082" ]
