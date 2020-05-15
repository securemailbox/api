from flask import Blueprint, jsonify, request, json
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DBAPIError

from ..models import Mailbox
from ..models import Message

from securemailbox import db

# Create the `send` blueprint
send_blueprint = Blueprint("send", __name__)


@send_blueprint.route("/send/", methods=["POST"])
def send():
    """
    Send a Message
    
    swagger_from_file: securemailbox/views/docs/send.yml
    """

        #get fingerprint
    if not request.is_json:
        return (
            jsonify(
                {"success": False, "error": "Request must be valid json", "data": None}
            ),
            400,
	)
    
    # get fingerprint
    fingerprint = request.json.get("fingerprint", None)
    if fingerprint is None:
        return jsonify({"success": False, "error": "no fingerprint"}), 400
    sender_fingerprint = request.json.get("sender_fingerprint", None)
    if sender_fingerprint is None:
        return jsonify({"success": False, "error": "no send fingerprint"}), 400
    message_t = request.json.get("message", None)
    if message_t is None:
        return jsonify({"success": False, "error": "no message"}), 400

    # update messages associated
    try:
        mailbox_id = (
            db.session.query(Mailbox.id).filter_by(fingerprint=fingerprint).first()
        )
    except NoResultFound:
        mailbox_id = None

    try:
        mailbox_send_id = (
            db.session.query(Mailbox.id)
            .filter_by(fingerprint=sender_fingerprint)
            .first()
        )
    except NoResultFound:
        mailbox_send_id = None
    # validity
    if mailbox_id is None:
        return (
            jsonify({"success": False, "error": "no recipient fingerprint match"}),
            400,
        )
    if mailbox_send_id is None:
        return jsonify({"success": False, "error": "no sender fingerprint match"}), 400

    try:
        message_ob = Message(
            message=message_t,
            sender_fingerprint=sender_fingerprint,
            mailbox_id=mailbox_id,
        )
        db.session.add(message_ob)
        db.session.commit()

        return jsonify({"success": True, "error": None}), 201
    except DBAPIError:
        return (
            jsonify({"success": False, "error": "message failed to add to messages"}),
            400,
        )

    # Catch all; there was an unknown error
    except BaseException as e:
        return jsonify({"success": False, "error": repr(e)}), 500
