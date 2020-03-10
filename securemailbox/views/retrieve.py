from flask import Blueprint, jsonify, request, json

from ..models import Mailbox

from securemailbox import db

# Create the `retrieve` blueprint
retrieve_blueprint = Blueprint("retrieve", __name__)

@retrieve_blueprint.route("/retrieve/", methods=["POST"])
def retrieve():

    # tables = db.get_tables_for_bind()
    # mailtest = tables[0](fingerprint='oihjuhqfd', is_active=True)
    # db.session.add(mailtest)
    # db.session.commit()
    # return jsonify({"mail1": False})

    # return jsonify({"success": True, "error": None})

    # print (request.is_json)
    # content = request.get_json()
    # print (content)
    # return 'JSON posted'
    
    # fingerprint = request.get_json("fingerprint", None)#("fingerprint", None)
    # print(fingerprint)
    # # if fingerprint == 12:
    # #     print('yep')
    # if fingerprint is None:
    #     return jsonify({"error": "fingerprint is none"}), 400

    # mailbox = Mailbox.query.filter_by(fingerprint=fingerprint)

    # messages = str(...)
    # return jsonify({"success": True, messages: messages, "error": None})
    ##############################################################

    # fingerprint = request.json.get("fingerprint", None)
    # fingerprint = request.get_json
    fingerprint = request.get_json("fingerprint")
    print(fingerprint)
    # if fingerprint is None:
        # return jsonify({'error': True}), 400

    print(request.method)

    print(request.data)

    print(request.args)

    print(request.form)

    print(request.is_json)

    content = request.json
    print (content)
    print()
    return jsonify({"success": True})
