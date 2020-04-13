import pytest

import securemailbox


@pytest.fixture
def client():
    securemailbox.app.config["TESTING"] = True

    with securemailbox.app.test_client() as client:
        yield client


def test_register(client):
    rv = client.post(
        "/register/", json={"fingerprint": "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF32"}
    )
    json_data = rv.get_json()
    assert json_data == {"success": True, "error": None, "data": {"mailbox": "FAC10F0C3D1D49F8F9A82CB553E79F7C92E1CF32"}}
