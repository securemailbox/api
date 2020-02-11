from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/register/", methods=["POST"])
def register():
    return jsonify({"success": True})

@app.route("/send/", methods=["POST"])
def send():
    return jsonify({"success": True})

@app.route("/retrieve/", methods=["POST"])
def retrieve():
    return jsonify({"success": True})

@app.route("/debug/")
def debug():
    return jsonify(fingerprints)

if __name__ == "__main__":
    app.run(debug=True)
