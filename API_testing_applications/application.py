import requests
import json

data = requests.get(url='http://127.0.0.1:8000/fetching/')
print(data.json())