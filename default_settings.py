from os import environ
from os.path import abspath, dirname, join

basedir = abspath(dirname(__file__))

### SQLAlchemy configuration details
# Docs: https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

user = environ['POSTGRES_USER']
pwd = environ['POSTGRES_PASSWORD']
db = environ['POSTGRES_DB']
host = 'db' # docker-compose creates a hostname alias with the service name
port = '5432' # default postgres port
SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % (user, pwd, host, port, db)

# Abort if we can't connect to the database
assert (
    SQLALCHEMY_DATABASE_URI is not None
), "expected `DATABASE_URL` environment variable to be set"

print(f"Connecting to database at '{SQLALCHEMY_DATABASE_URI}'")

SQLALCHEMY_TRACK_MODIFICATIONS = False
