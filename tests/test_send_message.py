import pytest

import securemailbox

from securemailbox.models import Mailbox
from securemailbox.models import Message

from securemailbox import db


test_fingerprint = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF33"

sender_test = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF33"

messaget = "test"


def test_send_message(client):
    new_mailbox = Mailbox(fingerprint=test_fingerprint)
    db.session.add(new_mailbox)
    db.session.commit()

    rv = client.post("/send/", json={"fingerprint": test_fingerprint, "sender_fingerprint": sender_test, "message": messaget})
    assert rv.get_json() == {
        "success": True,
        "error": None,
    }
    #above success match with below
    Id=db.session.query(Mailbox.id).filter_by(fingerprint=test_fingerprint).first()
    r_message=Message.query.filter_by(mailbox_id=Id).filter_by(message=messaget).first()
    #not sure how to get the message again directly from new_mailbox
    #r_message=new_mailbox
    assert r_message.message==messaget
   
