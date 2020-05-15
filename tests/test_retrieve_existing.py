import pytest

from flask import Blueprint, jsonify, request, json
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from securemailbox import db
from securemailbox.models import Mailbox, Message

test_fingerprint = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF33"


def test_retrieve_existing(client):
    rv = client.post("/retrieve/", json={"fingerprint": test_fingerprint})
    assert rv.get_json() == {
	    "success": True,
        "error": None,
        "data": {"count": 0, "messages": []},
    }
    
    #  
    #rv = client.post("/retrieve/", json={"fingerprint": test_fingerprint})
    #assert rv.get_json() == {
    #    "success": False,
    #    "error": f"mailbox with fingerprint '{test_fingerprint}' dosen't exists",
    #    "data": None,
    #}

#match above with data from below query?

    
    Id=db.session.query(Mailbox.id).filter_by(fingerprint=test_fingerprint).first()
    r_message=Message.query.filter_by(mailbox_id=Id).all()
    assert rv.data==r_message

