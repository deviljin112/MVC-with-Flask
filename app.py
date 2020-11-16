from flask import Flask

app = Flask(__name__)

students = [
    {
        "id": 0,
        "title": "Mr.",
        "first_name": "Dev",
        "last_name": "Something",
    },
]


@app.route("/")
def home():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)