import pytest

import securemailbox


def test_retrieve_no_json(client):
    rv = client.post("/retrieve/",)
    assert rv.get_json() == {
        "success": False,
        "error": "Request must be valid json",
    }
