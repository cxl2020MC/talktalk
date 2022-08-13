from itsdangerous import json
import requests

print(requests.post('https://talktalk-six.vercel.app/api/v1/talktalk', json = {'type': 'load'}).json())
data =  {'type': 'send', 'data': {
        'text': '测试测试',
        'device': 'vscode测试环境'
    }}
# print(requests.post('https://talktalk-six.vercel.app/api/v1/talktalk', json = data).json())