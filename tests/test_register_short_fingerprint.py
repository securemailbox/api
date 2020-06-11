import pytest

import securemailbox

short_fingerprint = "42"


def test_register_short_fingerprint(client):
    rv = client.post("/register/", json={"fingerprint": short_fingerprint})
    assert rv.get_json() == {
        "success": False,
        "error": "field 'fingerprint' is not a valid length.",
    }
