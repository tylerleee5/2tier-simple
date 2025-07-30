from flask import Flask, jsonify

app = Flask(__name__)
users = {
    "1": {"name": "Alice"},
    "2": {"name": "Bob"}
}

@app.route("/")
def home():
    return " Hello world! Welcome to the 2‑Tier App!"

@app.route("/users/<id>")
def get_user(id):
    return jsonify(users.get(id, {"error": "User not found"}))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
