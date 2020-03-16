from flask import Blueprint, jsonify, request

from securemailbox import db
from ..models import Mailbox, Message

# Create the `send` blueprint
send_blueprint = Blueprint("send", __name__)


@send_blueprint.route("/send/", methods=["POST"])
def send():
    # Ensure that the request is valid json
    if not request.is_json:
        return jsonify({"success": False, "error": "Request must be valid json"}), 400

    # Ensure that all required fields are present in the request body
    for field in ["fingerprint", "message", "sender"]:
        if request.json.get(field, None) is None:
            return (
                jsonify({"success": False, "error": f"field '{field}' is required."}),
                400,
            )
    try:
        fingerprint = request.json.get("fingerprint")
        mailbox = Mailbox.query.filter_by(fingerprint=fingerprint).first()
        if mailbox is None:
            return (
                jsonify(
                    {
                        "success": False,
                        "error": f"mailbox assosciated with fingerprint '{fingerprint}' doesn't esixt",
                    }
                ),
                404,
            )
        message = request.json.get("message")
        sender_fingerprint = request.json.get("sender")

        new_message = Message(message=message, sender_fingerprint=sender_fingerprint)

        mailbox.messages.append(new_message)
        # db.session.add(message)
        db.session.commit()
        return (
            jsonify(
                {
                    "success": True,
                    "error": None,
                    "data": {"message": new_message.message},
                }
            ),
            200,
        )
    # Catch all; there was an unknown error
    except BaseException as e:
        return jsonify({"success": False, "error": repr(e)}), 500
