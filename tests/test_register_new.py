import pytest

import securemailbox

test_fingerprint = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF32"


def test_register_new(client):
    rv = client.post("/register/", json={"fingerprint": test_fingerprint})
    assert rv.status_code == 201
    assert rv.get_json() == {
        "success": True,
        "error": None,
        "data": None
    }
