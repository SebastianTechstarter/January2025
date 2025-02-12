# Aufgabe 2
# Route 1: /user/<id>
# Beispiel: http://localhost:6060/user/1
# Rückgabe: Nutzerdetails wie {"id": 1, "name": "Alice", "email":
# "alice@example.com"}
from flask import Flask, request
import jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]


@app.route("/user/<int:id>")
def get_user_by_id(id):
    for user in users:
        if user["id"] == id:
            return jsonify(user)
    return jsonify({"message": f"User with the ID {id} not found."})


# Route 2: /login/<id>
# Beispiel: http://localhost:6060/login/2
# Rückgabe: "User Bob successfully logged in!" (oder Fehler, falls ID nicht
# existiert)
@app.route("/login/<int:id>")
def login_user(id):
    for user in users:
        if user["id"] == id:
            return jsonify({"message": f"User {user['name']} successfully logged in!"})
    return jsonify({"message": f"User with the ID {id} not found."})


# Route 3: /search?name=<name>
# Beispiel: http://localhost:6060/search?name=Charlie
# Rückgabe: "Found user: Charlie" oder "No user found with name: Charlie"
@app.route("/search")
def search_user_by_name():
    name = request.args.get("name")
    for user in users:
        if user["name"].lower() == name.lower():
            return jsonify({"message": f"Found user: {user['name']}"})
    return jsonify({"message": f"No user found with name: {name}"})
