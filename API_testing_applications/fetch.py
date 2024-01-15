import requests
import json

a = requests.get(url='http://127.0.0.1:8000/create/')
print(a.json())