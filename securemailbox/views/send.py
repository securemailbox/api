from flask import Blueprint, jsonify

from securemailbox import db

# Create the `send` blueprint
send_blueprint = Blueprint("send", __name__)

@send_blueprint.route("/send/", methods=["POST"])
def send():
    return jsonify({"success": True, "error": None})