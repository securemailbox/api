from flask import Blueprint, jsonify
from flask_swagger import swagger

from securemailbox import app, __version__

# Create the 'spec' blueprint
spec_blueprint = Blueprint("spec", __name__)

spec_url = "/spec/"

@spec_blueprint.route(spec_url, methods=["GET"])
def spec():
    swag = swagger(app, from_file_keyword='swagger_from_file')
    swag['info']['version'] = __version__
    swag['info']['title'] = "Secure Mailbox"
    return jsonify(swag)
