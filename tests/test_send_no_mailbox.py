import pytest

import securemailbox

from flask import Blueprint, jsonify, request, json
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from securemailbox import db
from securemailbox.models import Mailbox, Message


test_fingerprint = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF33"

sender_test = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF33"

message = "test"

def test_send_no_mailbox(client):
#below always causes failure,                                              
    rv = client.post("/send/", json={"fingerprint": test_fingerprint, "sender_fingerprint": sender_test, "message": message})                               
    assert rv.get_json() == {                                                 
        "success": False,                                                     
        "error": "no recipient fingerprint match",
    }
