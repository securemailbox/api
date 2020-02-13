from flask import Blueprint, jsonify

from app import db

# Create the `retrieve` blueprint
retrieve_blueprint = Blueprint("retrieve", __name__)

@register_blueprint.route("/retrieve/", methods=["POST"])
def retrieve():
    return jsonify({"success": True, "error": None})