from flask import Blueprint, jsonify, request

from ..models import Mailbox

from securemailbox import db

# Create the `retrieve` blueprint
retrieve_blueprint = Blueprint("retrieve", __name__)


@retrieve_blueprint.route("/retrieve/", methods=["POST"])
def retrieve():
    # Ensure that the request is valid json
    if not request.is_json:
        return jsonify({"success": False, "error": "Request must be valid json"}), 400

    # Ensure that all required fields are present in the request body
    for field in ["fingerprint"]:
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
        # Query all messages associated with the mailbox
        # TODO: Determine what should be done with all the messages
        # I.e. Are they deleted/archived? Are they marked as 'read'?
        messages = mailbox.messages.all()
        return (
            jsonify({"success": True, "error": None, "data": {"messages": messages}}),
            200,
        )

    # Catch all; there was an unknown error
    except BaseException as e:
        return jsonify({"success": False, "error": repr(e)}), 500
