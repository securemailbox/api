from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from securemailbox import db
from ..models import Mailbox
from ..constants import FINGERPRINT_LENGTH

# Create the `register` blueprint
# Docs:
register_blueprint = Blueprint("register", __name__)


@register_blueprint.route("/register/", methods=["POST"])
def register():
    # Ensure a valid request is received
    if not request.is_json:
        return jsonify({"success": False, "error": "Request must be valid json"}), 400

    # Ensure all fields in request are not NULL
    for field in ["fingerprint"]:
        field_to_check = request.json.get(field, None)
        if field_to_check is None:
            return (
                jsonify({"success": False, "error": f"field '{field}' is required."}),
                400,
            )
        if len(field_to_check) != FINGERPRINT_LENGTH:
            return (
                jsonify({"success": False, "error": f"field '{field}' is not a valid length."}),
                400,
            )
    try:
        incoming_fingerprint = request.json.get("fingerprint")
        new_mailbox = Mailbox(fingerprint=incoming_fingerprint)
        db.session.add(new_mailbox)
        db.session.commit()

        return (
            jsonify({"success": True, "error": None, "data": {"mailbox": new_mailbox.fingerprint}}),
            200,
        )
    except IntegrityError:
        return (
            jsonify(
                {
                    "success": False,
                    "error": f"mailbox with fingerprint '{incoming_fingerprint}' already exists",
                }
            ),
            400,
        )
    # Catch all; there was an unknown error
    except BaseException as e:
        return jsonify({"success": False, "error": repr(e)}), 500
