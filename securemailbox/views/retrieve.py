from flask import Blueprint, jsonify, request, json
from sqlalchemy.exc import IntegrityError

from ..models import Mailbox
from ..models import Message

from securemailbox import db

# Create the `retrieve` blueprint
retrieve_blueprint = Blueprint("retrieve", __name__)

@retrieve_blueprint.route("/retrieve/", methods=["POST"])
def retrieve():

    # Check for valid json request
    if not request.is_json:
        return jsonify({'success': False, 'error': 'Request must be valid json', 'data': None}), 400

    req_fingerprint = request.json.get('fingerprint', None)

    # Check if fingerprint is present in json request body
    if req_fingerprint is None:
        return jsonify({'success': False, 'error': 'fingerprint not in request', 'data': None}), 400

    # Check if fingerprint value is string variable
    if not isinstance(req_fingerprint, str):
        return jsonify({'success': False, 'error': 'fingerprint value not valid', 'data': None}), 400

    # search for fingerprint in mailbox table
    try:
        mailbox_id = Mailbox.query.filter_by(fingerprint=req_fingerprint).first()
    except IntegrityError:
        return jsonify({'success': False, 'error': 'Unknown error with fingerprint', 'data': None}), 400

    # check if mailbox_id is a valid entry before using it
    if mailbox_id is None:
        return jsonify({'success': False, 'error': 'fingerprint not in database', 'data': None}), 400    
    
    # set mailbox_num to id attribute
    mailbox_id = mailbox_id.id
    
    # if sender_fingerprint provided, it is set, otherwise None
    req_sender_fingerprint = request.json.get('sender_fingerprint', None)    

    # query for messages differently if sender_fingerprint is provided
    try:
        if req_sender_fingerprint:
            message_receive = Message.query.filter_by(mailbox_id=mailbox_id, sender_fingerprint=req_sender_fingerprint).all()
        else:
            message_receive = Message.query.filter_by(mailbox_id=mailbox_id).all()

    except IntegrityError:
        return jsonify({'success': False, 'error': 'Unknown error receiving messages', 'data': None}), 400

    except BaseException as e:
        return jsonify({"success": False, "error": repr(e)}), 500

    # return all fields of all related messages
    all_messages = []

    for message in message_receive:
        all_messages.append({
            "message": message.message,
            "sender_fingerprint": message.sender_fingerprint,
            "created_at": message.created_at,
            "updated_at": message.updated_at,
        })

    return (
        jsonify(
            {
                "success": True,
                "error": None,
                "data": {"messages": all_messages, "count": len(all_messages)},
            }
        ), 200
    )
