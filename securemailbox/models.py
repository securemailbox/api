from datetime import datetime

from sqlalchemy.dialects.postgresql import ARRAY

from . import db

# TODO: Determine what a good fingerprint length is
FINGERPRINT_LENGTH = 100


class Mailbox(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fingerprint = db.Column(db.String(FINGERPRINT_LENGTH), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    # One-to-many mailbox to messages relationship
    # Docs: https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#one-to-many-relationships
    messages = db.relationship("Message", backref="mailbox", lazy="dynamic")

    # Enable datetime support with `True`
    # Docs: https://docs.sqlalchemy.org/en/13/core/type_basics.html#sqlalchemy.types.DateTime.__init__
    created_at = db.Column(db.DateTime(True), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(True), default=datetime.utcnow)

    def __repr__(self):
        return f"<Mailbox {self.fingerprint}>"


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
<<<<<<< HEAD
        return f"<Message {self.message}>"
=======
        return f"<Message {self.message}"


class Art(db.Model):
    __tablename__ = "art"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    art = db.Column(db.Text, nullable=False)
    tags = db.Column(ARRAY(db.String))

    # Enable datetime support with `True`
    # Docs: https://docs.sqlalchemy.org/en/13/core/type_basics.html#sqlalchemy.types.DateTime.__init__
    created_at = db.Column(db.DateTime(True), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(True), default=datetime.utcnow)
>>>>>>> e1a4f8ba56ad28b12655f6c8ca4cabe9de1d539b
