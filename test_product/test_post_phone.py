from http.client import responses
import requests

url = 'http://127.0.0.1:8000/api/token/'
data = {
    'username':'admin',
    'password':'123456qwerty',
}

responses = requests.post(url, json=data)
print(responses.json())