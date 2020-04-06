from flask import Blueprint, jsonify, request

from securemailbox import db
from ..models import Mailbox
from ..models import Message

# Create the `register` blueprint
# Docs:
register_blueprint = Blueprint("register", __name__)


@register_blueprint.route("/register/", methods=["POST"])
def register():
    incoming_mailbox = request.get_json(force=True, silent=True)

    if incoming_mailbox is None or incoming_mailbox['fingerprint'] is None:
        return jsonify({"success": False, "error": ""})

    fetched_mailboxes = Mailbox.query.all()
    for fetched_mailbox in fetched_mailboxes:
        if fetched_mailbox['fingerprint'] == incoming_mailbox['fingerprint']:
            return jsonify({"success": False, "error": "fingerprint already exists"})
    db.session.add(incoming_mailbox)
    return jsonify({"success": True, "error": None})

