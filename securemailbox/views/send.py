
from flask import Blueprint, jsonify

from ..models import Mailbox
from ..models import Message

from securemailbox import db

# Create the `send` blueprint
send_blueprint = Blueprint("send", __name__)


@send_blueprint.route("/send/", methods=["POST"])
def send():

    #get fingerprint
    fingerprint = request.json.get("fingerprint", None)
    if fingerprint is None:
        return jsonify({"error": "no fingerprint"}), 400
    sender_fingerprint = request.json.get("sender_fingerprint", None)
    if sender_fingerprint is None:
        return jsonify({"error": "no send fingerprint"}), 400
    message_t = request.json.get("message", None)
    if message_t is None:
        return jsonify({"error": "no message"}), 400
    
    #update messages associated
    #not sure how to make the id unique and get current user fingerprint? clarification
    #needed/retrieve all ids to check for available? counter?
    #message not retrieved for testing purposes.

    mailbox = Mailbox.query.filter_by(fingerprint=fingerprint)

    #validity
    if mailbox is None:
        return jsonify({"error": "no fingerprint match"}), 400

    #make new message id
    #idbox = Message.query.all()

    #for x in idbox:
    #    if x == None:
    #        break

    #rplace 1 with x for available id number?
    
    message_ob = Message(id = 1, message=message_t,sender_fingerprint=sender_fingerprint, mailbox_id=mailbox.id)
    db.session.add(message_ob)
    db.session.commit()
    
    return jsonify({"success": True, "error": None})

    
    #return jsonify({"success": True, "error": None})
#messages in a mailbox instance is where message is added
#to what I have now implies message not within mailbox needs modification
