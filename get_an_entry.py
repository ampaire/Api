
from flask import Flask, jsonify, request,abort
app = Flask(__name__)

entries = [
    {
        'id_': 1,
        'Topic': "My Birthday",
        'Contents': "I had actually forgotten all about this day being my birthday." +
        "I got out of my room and all I got was a shower of my life." +
        "All my friends stood by the door with satisfied smiles watching me dripping wet."
    },
    {
        'id_': 2,
        'Topic': "Rachel's visit",
        'Contents': "Dear Diary, did I tell you about Rachel?. Racheal is my elder sister." +
        "She is the picky type and loves good food. So I spent the whole morning cooking" +
        "I had to literally scrub the whole house plus the ceiling... haha" +
        "She is the tidy one you know and strict hehe I mean strict about hygiene."
    }
]


@app.route("/",)
def index():
    return jsonify({'message': 'Here is your entry'})


@app.route("/api/v1/entries/<int:id_>", methods=["GET"])
def getEntry(id_):
    entry = [entry for entry in entries if entry['id_'] == id_]
    if len(entry) ==0:
        abort(404)
    return jsonify({'entry': entry})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
