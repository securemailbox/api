from flask import Blueprint, jsonify, request, json
from datetime import datetime
from ..models import Mailbox

from securemailbox import db

# Create the `register` blueprint
# Docs:
register_blueprint = Blueprint("register", __name__)


@register_blueprint.route("/register/", methods=["POST"])
def register():
    incoming_mailbox = request.get_json(force=True, silent=True)
    error = None
    incoming_fingerprint = incoming_mailbox['fingerprint']
    incoming_id = incoming_mailbox['id']
    if incoming_fingerprint or incoming_id is None:
        return jsonify({"success": False, "error": "missing required user information"})

    return jsonify({"success": True, "error": None})

# connected_db = db.get_db()
    # if connected_db.execute(
    #     'SELECT id FROM user WHERE fingerprint = ?', (fingerprint,)
    # ).fetchnone() is None:
    #     return jsonify({"success": False, "error": 'User is already registered.'})
    # created_at = datetime.now()
    # updated_at = datetime.now()
    # if error is None:
    #     connected_db.execute(
    #         'INSERT INTO Mailbox (fingerprint'
    #     )
