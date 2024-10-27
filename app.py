import requests
import json

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
        print(f'Error al obtener personas: {e}')
        return []
    except ValueError as e:
        print(f'Error al parsear JSON: {e}')
        return []

def main():
    people = get_people()
    with open('people.json', 'w') as f:
        json.dump(people, f)

if __name__ == '__main__':
    main()
