import pytest

import securemailbox

from securemailbox import db
from securemailbox.models import Mailbox, Message


test_fingerprint = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF33"

sender_test = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF33"

message = "test"


def test_delete_no_message(client):
    #no adding message no match
    new_mailbox = Mailbox(fingerprint=test_fingerprint)
    db.session.add(new_mailbox)
    db.session.commit()
    
    rv = client.post(
        "/delete/",
        json={
            "fingerprint": test_fingerprint,
            "sender_fingerprint": sender_test,
            "message": message,
	},
    )
    assert rv.get_json() == {
        "success": False,
	"error": "no matching message found",
    }
