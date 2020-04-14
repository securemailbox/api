import pytest

import securemailbox

test_fingerprint = "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF32"


def test_register_long_fingerprint(client):
    rv = client.post("/register/", json={"fingerprint": test_fingerprint + "123"})
    assert rv.get_json() == {
        "success": False,
        "error": "field 'fingerprint' is not a valid length.",
    }
