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

    # Check if fingerprint is present in json request body
    if 'fingerprint' not in data:
        return jsonify({'fingerprint not in request': True}), 400

    # search for fingerprint in mailbox table, assign to variable
    mailbox_num = Mailbox.query.filter_by(fingerprint=data['fingerprint']).first()

    # check if mailbox_num is a valid entry
    if mailbox_num is None:
        return jsonify({'fingerprint not in database': True}), 400    

    # set mailbox_num to id attribute
    mailbox_num = mailbox_num.id

    sender_is_present = False

    # check if sender_fingerprint is in request body
    if 'sender_fingerprint' in data:
        sender_is_present = True

    # query for messages differently if sender_fingerprint is provided
    if sender_is_present:
        message_receive = Message.query.filter_by(mailbox_id=mailbox_num, sender_fingerprint=data['sender_fingerprint']).all()
        if len(message_receive) == 0:
            return jsonify({'sender_fingerprint incorrect': True}), 400
        print('\tMessages in', data['fingerprint'], 'mailbox from sender', data['sender_fingerprint'],':')
    else:
        message_receive = Message.query.filter_by(mailbox_id=mailbox_num).all()
        print('\tMessages in', data['fingerprint'], 'mailbox:')

    # print messages, will change to response soon
    for i in range(len(message_receive)):
        print(message_receive[i].sender_fingerprint, ':', message_receive[i].message, flush=True)

    return jsonify({"success": True})
