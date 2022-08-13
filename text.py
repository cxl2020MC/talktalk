from itsdangerous import json
import requests

print(requests.post('https://talktalk-six.vercel.app/api/v1/talktalk', json = {'type': 'load'}).json())