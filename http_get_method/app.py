
from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
students = [
    {
        "id": 1,
        "name": "Prasanna",
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Arun",
        "course": "React"
    },
    {
        "id": 3,
        "name": "Kumar",
        "course": "Flask"
    }
]

# GET API
@app.route("/students", methods=["GET"])
def get_students():

    return jsonify(students), 200


if __name__ == "__main__":
    app.run(debug=True)
