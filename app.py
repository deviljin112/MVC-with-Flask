# Imports flask into the project
from flask import Flask, jsonify

# Creates a flask instance
app = Flask(__name__)

students = [
    {
        "id": 0,
        "title": "Mr.",
        "first_name": "Dev",
        "last_name": "Something",
    },
]


# Used to route traffic to this function
# "/" means home directory
@app.route("/")
def home():
    return "Hello World"


# This route will create a new GET route to our link
# accessible at http://127.0.0.1:5000/api/v1/student/data
@app.route("/api/v1/student/data", methods=["GET"])
def student_data():
    # ETL = Extract Transform Load
    return jsonify(students)  # Transforms data into JSON


if __name__ == "__main__":
    # Runs the application
    app.run(debug=True)
