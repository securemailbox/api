import pytest

import securemailbox

from flask import Blueprint, jsonify, request, json
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from securemailbox.models import Mailbox
from securemailbox.models import Message

from securemailbox import db


test_fingerprint = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF33"

sender_test = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF33"

messaget = "test"

def test_send_message(client):
    rv = client.post("/send/", json={"fingerprint": test_fingerprint, "sender_fingerprint": sender_test, "message": messaget})
    assert rv.get_json() == {
        "success": True,
        "error": None,
    }
    rv = client.post("/send/", json={"fingerprint": test_fingerprint, "sender_fingerprint": sender_test, "message": messaget})
    #above success match with below
    #try:
    Id=db.session.query(Mailbox.id).filter_by(fingerprint=test_fingerprint).first()
    r_message=Message.query.filter_by(mailbox_id=Id).filter_by(message=messaget).first()
    assert r_message.message==messaget
   # except IntegrityError:
       # return (
           # jsonify(
           #     {
          #          "success":False,
         #           "error":"un retrievable message",
        #        }
       #     ),
      #      400,
     #   )
    #return (
    #    jsonify(
   #         {
  #              "success":True,
 #               "error":None,
#	    }
  #      ),
 #       400,
#    )

    

    

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
