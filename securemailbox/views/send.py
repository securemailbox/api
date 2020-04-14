
from flask import Blueprint, jsonify, request, json
from sqlalchemy.orm.exc import NoResultFound

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
    try:
        mailbox_id = db.session.query(Mailbox.id).filter_by(fingerprint=fingerprint).first()
    except NoResultFound:
    mailbox_id = None    
    
    #validity
    if mailbox_id is None:
        return jsonify({"error": "no fingerprint match"}), 400

    mail = Message.query.filter_by(mailbox_id=mailbox_id) 

    message_ob = Message(message=message_t,sender_fingerprint=sender_fingerprint, mailbox_id=mailbox_id)
    db.session.add(message_ob)
    db.session.commit()
    
    return jsonify({"success": True, "error": None})

#messages in a mailbox instance is where message is added
#to what I have now implies message not within mailbox needs modification
