# app.py
from flask import Flask, jsonify, redirect, url_for
from flask.logging import create_logger
import requests

app = Flask(__name__)
logger = create_logger(app)

SWAPI_URL = 'https://swapi.dev/api/people/'

def get_people():
    try:
        response = requests.get(SWAPI_URL)
        response.raise_for_status()  # Lanza una excepción si el código de estado no es 200
        data = response.json()
        people = data['results']
        people.sort(key=lambda x: x['name'])
        return people
    except requests.exceptions.RequestException as e:
        logger.error(f'Error al obtener personas: {e}')
        return []
    except ValueError as e:
        logger.error(f'Error al parsear JSON: {e}')
        return []

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Bienvenido a la API de Star Wars. Para obtener la lista de personas, accede a /people'})

@app.route('/people', methods=['GET'])
def people():
    people = get_people()
    return jsonify(people)

if __name__ == '__main__':
    app.run(debug=True)
