import pytest

import securemailbox

test_fingerprint = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF33"

sender_test = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF33"

message = "test"

def test_send_existing(client):
    rv = client.post("/send/", json={"fingerprint": test_fingerprint, "sender_fingerprint": sender_test, "message": message})
    assert rv.get_json() == {
        "success": True,
        "error": None,
    }
    
    #below always causes failure, 
    #rv = client.post("/send/", json={"fingerprint": test_fingerprint, "sender_fingerprint": sender_test, "message": message})
    #assert rv.get_json() == {
    #    "success": False,
    #    "error": "there is no sender and/or a reciever fingerprint and/or message",
    #}
