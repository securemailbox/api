from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_swagger import swagger
__version__ = "0.8.0"

app = Flask(__name__)

# Load default config from ../default_settings.py
# Docs: https://flask.palletsprojects.com/en/1.1.x/config/
app.config.from_object("default_settings")

# Allow setting overrides from environment
# app.config.from_envvar("SECUREMAILBOX_SETTINGS")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import and register blueprints with app instance
# Docs: https://flask.palletsprojects.com/en/1.1.x/blueprints/
from securemailbox.views.register import register_blueprint
from securemailbox.views.send import send_blueprint
from securemailbox.views.retrieve import retrieve_blueprint

app.register_blueprint(register_blueprint)
app.register_blueprint(send_blueprint)
app.register_blueprint(retrieve_blueprint)

@app.route("/spec/")
def spec():
    swag = swagger(app, from_file_keyword='swagger_from_file')
    swag['info']['version'] = __version__
    swag['info']['title'] = "Secure Mailbox"
    return jsonify(swag)


# Create database tables
# Note: Model classes must be imported prior to this running
from .models import *

db.create_all()
