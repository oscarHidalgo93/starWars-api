from flask import Flask, jsonify
from starwars_api import get_people

app = Flask(__name__)

@app.route('/people', methods=['GET'])
def get_people_endpoint():
    people = get_people()
    people.sort(key=lambda x: x['name'])
    return jsonify(people)

if __name__ == '__main__':
    app.run(debug=True)


