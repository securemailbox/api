from flask import Blueprint, jsonify, request, json
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DBAPIError

from ..models import Mailbox
from ..models import Message

from securemailbox import db

# Create the `send` blueprint                                                  
delete_blueprint = Blueprint("delete", __name__)


@delete_blueprint.route("/delete/", methods=["POST"])
def delete():

    # get fingerprint                                                         
    if not request.is_json:
        return (
            jsonify({"success": False, "error": "Request must be valid json",}),
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
    	mailbox_id = None;

        # validity
    if mailbox_id is None:
        return (
    	    jsonify({"success": False, "error": "no recipient fingerprint match"}),
            400,
    	)

    try:
	message_id = (
            db.session.query(Message.id).filter_by(mailbox_id=mailbox_id, sender_fingerprint=sender_fingerprint,message=message_t).first()
        )
    except NoResultFound:
        message_id = None;

        # validity                                                             
    if message_id is None:
	return (
            jsonify({"success": False, "error": "no recipient fingerprint match"}),
            400,
        )

    try:
        db.session.delete(message_id)
        db.session.commit()
