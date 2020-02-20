
from securemailbox import db

# TODO: Determine what a good fingerprint length is
FINGERPRINT_LENGTH = 100

class Mailbox(db.model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fingerprint = db.Column(db.String(FINGERPRINT_LENGTH), unique=True)
    is_active = db.Column(db.Boolean)
    
    created_at = db.Column(db.DateTime(True), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(True), default=datetime.utcnow)

class Message(db.model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String(1000))
    sender_fingerprint = db.Column(db.String(FINGERPRINT_LENGTH))

    # TODO: Determine relationship to mailbox model
    created_at = db.Column(db.DateTime(True), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(True), default=datetime.utcnow)