import requests
import json

url = 'http://127.0.0.1:8000/create/'

data = {
    'id':5,
    'name':'Rohit Shelar',
    'age':55,
    'city':'Thane'
}

jdata = json.dumps(data)

reply = requests.put(url, data=jdata)

print(reply.json())