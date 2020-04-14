import pytest

import securemailbox

test_fingerprint = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF33"


def test_register_existing(client):
    rv = client.post("/register/", json={"fingerprint": test_fingerprint})
    assert rv.get_json() == {
        "success": True,
        "error": None,
        "data": {"mailbox": test_fingerprint},
    }
    rv = client.post("/register/", json={"fingerprint": test_fingerprint})
    assert rv.get_json() == {
        "success": False,
        "error": f"mailbox with fingerprint '{test_fingerprint}' already exists",
    }
