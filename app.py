from flask import Flask, render_template, jsonify
from flask.logging import create_logger
import requests
import json

SWAPI_URL = 'https://swapi.dev/api/people/ '

def get_people():
    try:
        response = requests.get(SWAPI_URL)
        response.raise_for_status()  # Lanza una excepción si el código de estado no es 200
        data = response.json()
        people = data['results']
        people.sort(key=lambda x: x['name'])
        return people
    except requests.exceptions.RequestException as e:
        print(f'Error al obtener personas: {e}')
        return []
    except ValueError as e:
        print(f'Error al parsear JSON: {e}')
        return []

def generate_people_json():
    people = get_people()
    with open('people.json', 'w') as f:
        json.dump(people, f)

generate_people_json()

app = Flask(__name__)
logger = create_logger(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/people', methods=['GET'])
def people():
    with open('people.json', 'r') as f:
        people = json.load(f)
    return jsonify(people)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
