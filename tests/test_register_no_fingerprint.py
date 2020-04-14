import pytest

import securemailbox


def test_register_no_fingerprint(client):
    rv = client.post("/register/", json={})
    assert rv.get_json() == {
        "success": False,
        "error": "field 'fingerprint' is required.",
    }
