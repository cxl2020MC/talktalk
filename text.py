from itsdangerous import json
import requests

print(requests.post('http://127.0.0.1:5000/api/v1/talktalk', json = {'type': 'load'}).json())