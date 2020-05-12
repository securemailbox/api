import pytest

import securemailbox

from flask import Blueprint, jsonify, request, json
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from /home/tom/api/securemailbox/models.py import Mailbox
from /home/tom/api/securemailbox/models.py import Message

from securemailbox import db


test_fingerprint = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF33"


def test_retrieve_existing(client):

    
    
    rv = client.post("/retrieve/", json={"fingerprint": test_fingerprint})
    rv = client.post("/retrieve/", json={"fingerprint": test_fingerprint})
    assert rv.get_json() == {
        "success": False,
        "error": f"mailbox with fingerprint '{test_fingerprint}' dosen't exists",
    }

    rv = client.post("/retrieve/", json={"fingerprint": test_fingerprint})
#match above with data from below query?

    try:
        Id=db.session.query(Mailbox.id).filter_by(fingerprint=test_fingerprint).first()
        r_message=Message.query.filter_by(mailbox_id=mailbox_id).all()
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
    if (r_message == 
    return (
        jsonify(
            {
                "success":True,
                "error":None,
            }
        ),
        400,
    )

