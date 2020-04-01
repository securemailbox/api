from flask import Blueprint, jsonify, request

from securemailbox import db
from ..models import Art

ascii_art_blueprint = Blueprint("ascii_art", __name__)


@ascii_art_blueprint.route("/art/new", methods=["POST"])
def create():
    required_keys = ["art"]
    body = request.json
    if not all(key in body for key in required_keys):
        print(key)
        pass

    return jsonify({"success": True, "error": None})


@ascii_art_blueprint.route("/art/", methods=["GET"])
def get():
    try:
        all_art = Art.query.limit(1).all()
        print(all_art)
    except Exception as e:
        return jsonify({"data": None, "error": str(e)}), 400

    return jsonify({"data": all_art, "error": None})


@ascii_art_blueprint.route("/art/<int:art_id>", methods=["GET"])
def get_one(art_id):

    try:
        art = Art.query.filter_by(id=art_id).first()
    except Exception as e:
        return jsonify({"data": None, "error": str(e)}), 400
    else:
        if art is None:
            return (
                jsonify(
                    {
                        "data": None,
                        "error": f"the piece of art with id '{art_id}'' does not exist",
                    }
                ),
                404,
            )

    return jsonify({"data": art, "error": None})


@ascii_art_blueprint.route("/art/update", methods=["PUT"])
def update():
    return jsonify({"success": True, "error": None})


@ascii_art_blueprint.route("/art/remove", methods=["DELETE"])
def delete():
    return jsonify({"success": True, "error": None})
