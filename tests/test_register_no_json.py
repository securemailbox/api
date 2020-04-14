import pytest

import securemailbox


def test_register_no_json(client):
    rv = client.post("/register/",)
    assert rv.get_json() == {
        "success": False,
        "error": "Request must be valid json",
    }
