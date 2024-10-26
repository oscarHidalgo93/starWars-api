from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/people', methods=['GET'])
def get_people():
    try:
        response = requests.get('https://swapi.dev/api/people/')
        data = response.json()
        sorted_data = sorted(data['results'], key=lambda x: x['name'])
        return jsonify(sorted_data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)