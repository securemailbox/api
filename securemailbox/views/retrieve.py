from flask import Blueprint, jsonify, request

from ..models import Mailbox

from securemailbox import db

# Create the `retrieve` blueprint
retrieve_blueprint = Blueprint("retrieve", __name__)


@retrieve_blueprint.route("/retrieve/", methods=["POST"])
def retrieve():

    fingerprint = request.json.get("fingerprint", None)
    if fingerprint is None:
        return jsonify({"error": "fingerprint is none"}), 400

    mailbox = Mailbox.query.filter_by(fingerprint=fingerprint)

    messages = str(...)
    return jsonify({"success": True, messages: messages, "error": None})
