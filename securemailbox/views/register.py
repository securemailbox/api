from flask import Blueprint, jsonify, request

from securemailbox import db
from ..models import Mailbox

# Create the `register` blueprint
# Docs:
register_blueprint = Blueprint("register", __name__)


@register_blueprint.route("/register/", methods=["POST"])
def register():
    incoming_mailbox = request.get_json(force=True, silent=True)

    if incoming_mailbox is None:
        return jsonify({"success": False, "error": "No register data received."})
    if incoming_mailbox['fingerprint'] is None:
        return jsonify({"success": False, "error": "No fingerprint received."})
    try:
        new_mailbox = Mailbox(incoming_mailbox)
        db.session.add(new_mailbox)
        return jsonify({"success": True, "error": None})
    except IntegrityError:
        return jsonify({"success": True, "error": "Mailbox already exists"})

