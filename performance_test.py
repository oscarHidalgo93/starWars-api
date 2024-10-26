import requests

def test_performance():
    url = 'http://starwars-microservice:80/people'
    response = requests.get(url)
    assert response.status_code == 200

if __name__ == '__main__':
    test_performance()