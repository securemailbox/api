from datetime import datetime

from . import db

# TODO: Determine what a good fingerprint length is
FINGERPRINT_LENGTH = 100

class Mailbox(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fingerprint = db.Column(db.String(FINGERPRINT_LENGTH), unique=True, nullable=False)
    is_active = db.Column(db.Boolean)

    messages = db.relationship("Message", backref="mailbox", lazy=True)

    
    # Enable datetime support with `True`
    # Docs: https://docs.sqlalchemy.org/en/13/core/type_basics.html#sqlalchemy.types.DateTime.__init__
    created_at = db.Column(db.DateTime(True), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(True), default=datetime.utcnow)

    def __repr__(self):
        return f"<Mailbox {self.fingerprint}"

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.Text, nullable=False)
    sender_fingerprint = db.Column(db.String(FINGERPRINT_LENGTH))

    mailbox_id = db.Column(db.Integer, db.ForeignKey("mailbox.id"), nullable=False)

    # Enable datetime support with `True`
    # Docs: https://docs.sqlalchemy.org/en/13/core/type_basics.html#sqlalchemy.types.DateTime.__init__
    created_at = db.Column(db.DateTime(True), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(True), default=datetime.utcnow)

    def __repr__(self):
        return f"<Message {self.message}"