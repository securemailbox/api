from datetime import datetime

from . import db

# TODO: Determine what a good fingerprint length is
FINGERPRINT_LENGTH = 100

class Mailbox(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fingerprint = db.Column(db.String(FINGERPRINT_LENGTH), unique=True)
    is_active = db.Column(db.Boolean)
    
    # Enable datetime support with `True`
    # Docs: https://docs.sqlalchemy.org/en/13/core/type_basics.html#sqlalchemy.types.DateTime.__init__
    created_at = db.Column(db.DateTime(True), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(True), default=datetime.utcnow)

    def __repr__(self):
        return '<Mailbox %r>' % self.fingerprint

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.Text)
    sender_fingerprint = db.Column(db.String(FINGERPRINT_LENGTH))

    # TODO: Determine relationship to mailbox model

    # Enable datetime support with `True`
    # Docs: https://docs.sqlalchemy.org/en/13/core/type_basics.html#sqlalchemy.types.DateTime.__init__
    created_at = db.Column(db.DateTime(True), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(True), default=datetime.utcnow)

    def __repr__(self):
        return '<Message %r>' % self.message