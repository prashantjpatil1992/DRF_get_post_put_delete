import requests
import json

url = 'http://127.0.0.1:8000/create/'

data = {
    'name':'RRRRRRRRRRRR',
    'age' : 34,
    'city':'Thane'
}

data = json.dumps(data)

a = requests.post(url,data=data)

print(a.json())

