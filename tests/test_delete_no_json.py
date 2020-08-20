import pytest

import securemailbox


def test_delete_no_json(client):
    rv = client.post("/delete/",)
    assert rv.get_json() == {
        "success": False,
        "error": "Request must be valid json",
    }
