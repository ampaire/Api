from flask import Flask, jsonify, request
from datetime import date
app = Flask(__name__)


@app.route("/",)
def index():
    return jsonify({'message': 'Welcome to your entries page'})


@app.route("/api/v1/entries", methods=["POST"])
def add_entry():
        entry = {
        "id_": entries[-1]['id_']+1,
        'now': datetime.utcnow(),
        "Topic": request.json['Topic'],
        "Contents": request.json.get('Contents', "")}
    entries.append(entry)
    if len(entry) == 0:
      return "missing data"
    return jsonify({'entries': entries})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
