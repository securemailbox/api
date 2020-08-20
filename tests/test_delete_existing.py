import pytest

import securemailbox

from securemailbox import db
from securemailbox.models import Mailbox, Message


test_fingerprint = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF33"

sender_test = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF33"

message = "test"

def test_delete_existing(client):
    #make mailbox and message
    new_mailbox = Mailbox(fingerprint=test_fingerprint)
    db.session.add(new_mailbox)

    try:
        mailbox_id = (
            db.session.query(Mailbox.id).filter_by(fingerprint=test_fingerprint).first()
        )
    except NoResultFound:
        mailbox_id = None

    if mailbox_id is None:
        return (
            jsonify({"success": False, "error": "no recipient fingerprint match"}),
            400,
        )    
    message_ob = Message(
        message=message,
        sender_fingerprint=sender_fingerprint,
        mailbox_id=mailbox_id,
    )
    db.session.add(message_ob)    
    db.session.commit()

    rv = client.post(
        "/delete/",
	json={
            "fingerprint": test_fingerprint,
            "sender_fingerprint": sender_test,
            "message": message,
	},
    )
    assert rv.get_json() == None
