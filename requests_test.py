import requests

data = {
    'name': 'germey',
    'age': 22
}
r = requests.get('https://httpbin.org/get', params=data)
print(r.json())