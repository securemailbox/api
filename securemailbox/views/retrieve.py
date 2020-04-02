from flask import Blueprint, jsonify, request, json

from ..models import Mailbox
from ..models import Message

from securemailbox import db

# Create the `retrieve` blueprint
retrieve_blueprint = Blueprint("retrieve", __name__)

@retrieve_blueprint.route("/retrieve/", methods=["POST"])
def retrieve():

    # #######################
    # # Testing mailbox add
    # mail = Mailbox(fingerprint='qwe')
    # db.session.add(mail)
    # mail = Mailbox(fingerprint='asd')
    # db.session.add(mail)
    # mail = Mailbox(fingerprint='zxc')
    # db.session.add(mail)
    # mail = Mailbox(fingerprint='bnm')
    # db.session.add(mail)

    # db.session.commit()

    # # Testing message add
    # mess = Message(message='message from qwe to asd', 
    #     sender_fingerprint='qwe',
    #     mailbox_id=2)
    # db.session.add(mess)

    # mess = Message(message='message from zxc to asd', 
    #     sender_fingerprint='zxc',
    #     mailbox_id=2)
    # db.session.add(mess)

    # mess = Message(message='message from bnm to asd', 
    #     sender_fingerprint='bnm',
    #     mailbox_id=2)
    # db.session.add(mess)

    # mess = Message(message='message from asd to qwe', 
    #     sender_fingerprint='asd',
    #     mailbox_id=1)
    # db.session.add(mess)

    # db.session.commit()
    # #######################

    data = request.get_json(force=True, silent=True)
    
    if data is None:
        return jsonify({"Invalid JSON": True}), 400
    else:
        # Check if all the necessary fields exist before making the database calls
        if 'fingerprint' in data:
            # Check if length is valid, not empty
            if len(data['fingerprint']) < 1:
                return jsonify({"Invalid Length of Item": True}), 400 
        else:
            return jsonify({'Not all data present': True}), 400

    mailbox_num = Mailbox.query.filter_by(fingerprint=data['fingerprint']).first()
    if mailbox_num is None:
        return jsonify({'fingerprint not in database': True}), 400

    mailbox_num = mailbox_num.id
    sender_is_present = False
    if 'sender_fingerprint' in data:
        if len(data['sender_fingerprint']) < 1:
            return jsonify({"Invalid Length of Item": True}), 400
        sender_is_present = True

    if sender_is_present:
        message_receive = Message.query.filter_by(mailbox_id=mailbox_num, sender_fingerprint=data['sender_fingerprint']).all()
        if len(message_receive) < 1:
            return jsonify({'sender_fingerprint incorrect': True}), 400
        print('\tMessages in', data['fingerprint'], 'mailbox from sender', data['sender_fingerprint'],':')
    else:
        message_receive = Message.query.filter_by(mailbox_id=mailbox_num).all()
        if len(message_receive) < 1:
            return jsonify({'sender_fingerprint incorrect': True}), 400
        print('\tMessages in', data['fingerprint'], 'mailbox:')

    for i in range(len(message_receive)):
        print(message_receive[i].sender_fingerprint, ':', message_receive[i].message, flush=True)

    return jsonify({"success": True})
