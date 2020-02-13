from os import environ
from os.path import abspath, dirname, join

basedir = abspath(dirname(__file__))

### SQLAlchemy configuration details
# Docs: https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL", None)

# Abort if we can't connect to the database
assert SQLALCHEMY_DATABASE_URI is not None, "expected `DATABASE_URL` environment variable to be set"

print(f"Connecting to database at '{SQLALCHEMY_DATABASE_URI}'")

SQLALCHEMY_TRACK_MODIFICATIONS = False