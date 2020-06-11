import pytest

from securemailbox import db
from securemailbox.models import Mailbox, Message

test_fingerprint = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF33"


def test_retrieve_existing(client):
    new_mailbox = Mailbox(fingerprint=test_fingerprint)
    db.session.add(new_mailbox)
    db.session.commit()

    rv = client.post("/retrieve/", json={"fingerprint": test_fingerprint})
    assert rv.get_json() == {
        "success": True,
        "error": None,
        "data": {"count": 0, "messages": []},
    }

    # turn below into database retrieval match? commenting for now
    # assert rv.data== b'{"data":{"count":0,"messages":[]},"error":null,"success":true}\n'
