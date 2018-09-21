from flask import Flask, jsonify, request
app = Flask(__name__)

entries = [
    {
        'id': 1,
        'Topic': "My Birthday",
        'Contents': "I had actually forgotten all about this day being my birthday." +
        "I got out of my room and all I got was a shower of my life." +
        "All my friends stood by the door with satisfied smiles watching me dripping wet."
    },
    {
        'id': 2,
        'Topic': "Rachel's visit",
        'Contents': "Dear Diary, did I tell you about Rachel?. Racheal is my elder sister." +
        "She is the picky type and loves good food. So I spent the whole morning cooking" +
        "I had to literally scrub the whole house plus the ceiling... haha" +
        "She is the tidy one you know and strict hehe I mean strict about hygiene."
    }
]


@app.route("/",)
def index():
    return jsonify({'message': 'Welcome to your entries page'})


@app.route("/api/v1/entries", methods=["POST"])
def add_entry():
    entry = {
        "id": entries[-1]['id']+1,
        "Topic": request.json.get('Topic'),
        "Contents": request.json.get('Contents', "")}
    entries.append(entry)
    return jsonify({'entries': entries})


@app.route("/api/v1/entries", methods=["GET"])
def get_entries():

    return jsonify({'entries': entries})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
