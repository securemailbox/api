from flask import Blueprint, jsonify

from securemailbox import db

# Create the `register` blueprint
# Docs: 
register_blueprint = Blueprint("register", __name__)

@register_blueprint.route("/register/", methods=["POST"])
def register():
    return jsonify({"success": True, "error": None})