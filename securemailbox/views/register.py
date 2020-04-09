from flask import Blueprint, jsonify, request
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

from securemailbox import db
from ..models import Mailbox

# Create the `register` blueprint
# Docs:
register_blueprint = Blueprint("register", __name__)


@register_blueprint.route("/register/", methods=["POST"])
def register():
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

        new_mailbox = Mailbox(fingerprint=fingerprint)
        db.session.add(new_mailbox)
        db.session.commit()

        return (
            jsonify({"success": True, "error": None, data: {"mailbox": new_mailbox}}),
            200,
        )
    except IntegrityError:
        return (
            jsonify(
                {
                    "success": False,
                    "error": f"mailbox with fingerprint '{fingerprint}' already exists",
                }
            ),
            400,
        )
    # Catch all; there was an unknown error
    except BaseException as e:
        return jsonify({"success": False, "error": repr(e)}), 500
