
from flask import Flask, jsonify, request

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


# POST API
@app.route("/students", methods=["POST"])
def create_student():

    data = request.get_json()

    new_student = {
        "id": len(students) + 1,
        "name": data["name"],
        "course": data["course"]
    }

    students.append(new_student)

    return jsonify(new_student), 201


# PUT API
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):

    data = request.get_json()

    for student in students:

        if student["id"] == student_id:

            student["name"] = data["name"]
            student["course"] = data["course"]

            return jsonify({
                "message": "Student updated successfully",
                "student": student
            }), 200

    return jsonify({
        "error": "Student not found"
    }), 404



# PATCH API
@app.route("/students/<int:student_id>", methods=["PATCH"])
def patch_student(student_id):

    data = request.get_json()

    for student in students:

        if student["id"] == student_id:

            if "name" in data:
                student["name"] = data["name"]

            if "course" in data:
                student["course"] = data["course"]

            return jsonify({
                "message": "Student partially updated successfully",
                "student": student
            }), 200

    return jsonify({
        "error": "Student not found"
    }), 404



# DELETE API
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            return jsonify({
                "message": "Student deleted successfully",
                "student": student
            }), 200

    return jsonify({
        "error": "Student not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)
