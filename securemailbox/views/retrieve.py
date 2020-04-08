from flask import Blueprint, jsonify, request, json

from ..models import Mailbox
from ..models import Message

from securemailbox import db

# Create the `retrieve` blueprint
retrieve_blueprint = Blueprint("retrieve", __name__)

@retrieve_blueprint.route("/retrieve/", methods=["POST"])
def retrieve():

    data = request.get_json(force=True, silent=True)

    if data is None:
        return jsonify({'success': False, 'error': 'Request must be valid json', 'data': None}), 400

    # Check if fingerprint is present in json request body
    if 'fingerprint' not in data:
        return jsonify({'success': False, 'error': 'fingerprint not in request', 'data': None}), 400

    # search for fingerprint in mailbox table, assign to variable
    mailbox_num = Mailbox.query.filter_by(fingerprint=data['fingerprint']).first()

    # check if mailbox_num is a valid entry
    if mailbox_num is None:
        return jsonify({'success': False, 'error': 'fingerprint not in database', 'data': None}), 400    

    # set mailbox_num to id attribute
    mailbox_num = mailbox_num.id

    sender_is_present = False

    # check if sender_fingerprint is in request body
    if 'sender_fingerprint' in data:
        sender_is_present = True

    # query for messages differently if sender_fingerprint is provided
    if sender_is_present:
        message_receive = Message.query.filter_by(mailbox_id=mailbox_num, sender_fingerprint=data['sender_fingerprint']).all()
    else:
        message_receive = Message.query.filter_by(mailbox_id=mailbox_num).all()

    # return all fields of all related messages
    all_messages = []

    for i in range(len(message_receive)):
        message_dict = {}
        message_dict["message"] = message_receive[i].message
        message_dict["sender_fingerprint"] = message_receive[i].sender_fingerprint
        message_dict["created_at"] = message_receive[i].created_at
        message_dict["updated_at"] = message_receive[i].updated_at

        all_messages.append(message_dict)

    return (
        jsonify(
            {
                "success": True,
                "error": None,
                "data": {"messages": all_messages, "count": len(all_messages)},
            }
        ), 200
    )