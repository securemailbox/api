import pytest

import securemailbox

from flask import Blueprint, jsonify, request, json
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from /home/tom/api/securemailbox/models.py import Mailbox
from /home/tom/api/securemailbox/models.py import Message

from securemailbox import db


test_fingerprint = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF33"

sender_test = "me"

message = "test"

def test_send_existing(client):
    rv = client.post("/send/", json={"fingerprint": test_fingerprint, "sender_fingerprint": sender_test, "message": message})
    assert rv.get_json() == {
        "success": False,
        "error": "no message or fingerprint",
    }
    rv = client.post("/send/", json={"fingerprint": test_fingerprint, "sender_fingerprint": sender_test, "message": message})
    #above success match with below
    try:
        Id=db.session.query(Mailbox.id).filter_by(fingerprint=test_fingerprint).first()
        r_message=Message.query.filter_by(mailbox_id=mailbox_id and message=message).first()
    except IntegrityError:
        return (
            jsonify(
                {
                    "success":False,
                    "error":"un retrievable message",
                }
            ),
            400,
        )
    return (
        jsonify(
            {
                "success":True,
                "error":None,
	    }
        ),
        400,
    )

    

    

    #rv = client.post("/send/", json={"fingerprint": test_fingerprint, "sender_fingerprint": sender_test, "message": message})
    #assert rv.get_json() == {
    #    "success": False,
	#"error": "sending failed for some reason",
    #}

    #rv2 = client.post("/retrieve/", json={"fingerprint": test_fingerprint})
    #assert rv2.get_json() == {
    #    "success": True,
    #    "error": None,
        #not sure how to check the message itself.
    #}
