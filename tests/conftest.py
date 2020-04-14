import pytest

import securemailbox


@pytest.fixture
def client():
    securemailbox.app.config["TESTING"] = True

    with securemailbox.app.test_client() as client:
        yield client
