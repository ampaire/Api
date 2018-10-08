from flask import Flask, jsonify, request
app = Flask(__name__)
import datetime


entries = [
    {
        'id': 1,
        'date':'02-04-2018',
        'Topic': "Not today",
        'Contents': "I hate late nights......"
    },
    {
        'id': 2,
        'date':'03-04-2018',
        'Topic': "When did I grow taller",
        'Contents': "I am not tall stop kidding me...."
    }
]


@app.route("/",)
def index():
    return 'Welcome to your entries page'



@app.route("/api/v1/entries", methods=["GET"])
def get_entries():

    return jsonify({'entries': entries})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
