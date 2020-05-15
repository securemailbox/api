import pytest

import securemailbox
from securemailbox.models import Message, Mailbox


@pytest.fixture
def client():
    securemailbox.app.config["TESTING"] = True

    with securemailbox.app.test_client() as client:
        yield client

# Force fixture to be used if not explicitly imported
@pytest.fixture(autouse=True)
def clean_database():
    # Delete all messages first so mailbox doesn't fail on cascade
    Message.query.delete()
    # Delete all mailboxes
    Mailbox.query.delete()

    yield