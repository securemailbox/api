from flask import Flask, jsonify, request

app = Flask(__name__)

fingerprints = {}

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/register/", methods=["POST"])
def register():
    fingerprint = request.json.get("fingerprint")
    fingerprints[fingerprint] = {
        "messages": []
    }
    return jsonify({"success": True})

@app.route("/send/", methods=["POST"])
def send():
    fingerprint = request.json.get("fingerprint")
    message = request.json.get("message")

    # Make sure user exists before trying to add a message
    if (user := fingerprints.get(fingerprint, None)) is not None:
        messages = user.get("messages")
        messages.append(message)
        return jsonify({"success": True})
    else:
        return jsonify({"error": f"user with fingerprint '{fingerprint}' does not exist"}), 404

@app.route("/retrieve/", methods=["POST"])
def retrieve():
    fingerprint = request.json.get("fingerprint")

        # Make sure user exists before trying to add a message
    if (user := fingerprints.get(fingerprint, None)) is not None:
        messages = user.get("messages")
        return jsonify({"messages": messages})
    else:
        return jsonify({"error": f"user with fingerprint '{fingerprint}' does not exist"}), 404

@app.route("/debug/")
def debug():
    return jsonify(fingerprints)

if __name__ == "__main__":
    app.run(debug=True)
