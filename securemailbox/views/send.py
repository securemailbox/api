
from flask import Blueprint, jsonify

from ..models import Mailbox
from ..models import Message

from securemailbox import db

# Create the `send` blueprint
send_blueprint = Blueprint("send", __name__)


@send_blueprint.route("/send/", methods=["POST"])
def send():

    #get fingerprint/check if can retrieve.validity
    fingerprint = request.json.get("fingerprint", None)
    if fingerprint is None:
        return jsonify({"error": "no fingerprint"}), 400
    #update messages associated
    #not sure how to make the id unique and get current user fingerprint? clarification
    #needed/retrieve all ids to check for available? counter?
    #message not retrieved for testing purposes.
    message = Message(id = 1, message="test1",sender_fingerprint=fingerprint, mailbox_id=1)
    db.session.add(message)
    db.session.commit()
    
    return jsonify({"success": True, "error": None})

    
    #return jsonify({"success": True, "error": None})
