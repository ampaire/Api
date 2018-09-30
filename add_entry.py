from flask import Flask, jsonify, request
import datetime
app = Flask(__name__)

entries = [
    {
        'id_': 1,
        'date': '22-09-2018',
        'Topic': 'Singing is not my hobby.',
        'Contents': 'Diary you know that moment you are asked to sing at a birthday? Gross'
    },
    {
        'id_': 2,
        'date': '23-09-2018',
        'Topic': 'September blues',
        'Contents': 'Yes september blues'


    }
]


@app.route("/",)
def index():
    return jsonify({'message': 'Welcome to your entries page'})


@app.route("/api/v1/entries", methods=["POST"])
def add_entry():

    if not request.json:
        return 'Invalid input format'
    
        entry = {

          "id_": entries[-1]['id_']+1,
          'date': datetime.datetime.today(),
          "Topic": request.json['Topic'],
          "Contents": request.json.get('Contents', "")
        }

    entries.append(entry)
    if len(entry) == 0:
      return "missing data"
    return jsonify({'entries': entries})



if __name__ == "__main__":
    app.run(debug=True, port=8080)
