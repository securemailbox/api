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
        return jsonify({"Invalid JSON": True}), 400
    else:
        # Check if all the necessary fields exist before making the database calls
        if 'mailbox_id' in data:
            # Check if length is valid, not empty
            if len(data['mailbox_id']) < 1:
                return jsonify({"Invalid Length of Item": True}), 400 
        else:
            return jsonify({'Not all data present': True}), 400

    mailbox_num = data['mailbox_id']
    
    # Testing mailbox add and delete
    # mail = Mailbox(fingerprint='qw', is_active=True)
    # db.session.add(mail)
    # # delete_mail = Mailbox.query.filter_by(id='1').first()
    # # db.session.delete(delete_mail)
    # db.session.commit()

    # Testing message add
    # mess = Message(message='new encrypted message right here', sender_fingerprint='1234',
    #     mailbox_id=6)
    # db.session.add(mess)
    # db.session.commit()

    # Testing getting multiple messages
    message_receive = Message.query.filter_by(mailbox_id=mailbox_num).all()
    for i in range(len(message_receive)):
        print(message_receive[i].sender_fingerprint, message_receive[i].message, flush=True)

    return jsonify({"success": True})
