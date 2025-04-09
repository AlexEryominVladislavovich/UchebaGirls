import requests

url = 'http://127.0.0.1:8000/api/v1/cars/1/'
data = {
    'info':'196'
}
response = requests.patch(url, json=data)
print(response.json(), response.text)