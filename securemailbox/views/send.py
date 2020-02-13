from flask import Blueprint, jsonify

from app import db

# Create the `send` blueprint
send_blueprint = Blueprint("send", __name__)

@register_blueprint.route("/send/", methods=["POST"])
def send():
    return jsonify({"success": True, "error": None})