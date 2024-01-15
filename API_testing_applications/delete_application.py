import requests
import json

url = 'http://127.0.0.1:8000/create/'

data = {
    'id':2
}

data = json.dumps(data)

a = requests.delete(url,data=data)

print(a.json())