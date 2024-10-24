import requests

def get_people():
    response = requests.get('https://swapi.dev/api/people/')
    return response.json()['results']
