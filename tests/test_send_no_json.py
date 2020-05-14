import pytest

import securemailbox


def test_send_no_json(client):
    rv = client.post("/send/",)
    assert rv.get_json() == {
        "success": False,
        "error": "Request must be valid json",
        "data":None,
    }
