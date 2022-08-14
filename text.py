from itsdangerous import json
import requests

# print(requests.post('https://talktalk-six.vercel.app/api/v1/talktalk', json = {'type': 'load'}).json())
data =  {'type': 'send', 'data': {
        'text': '测试测试',
        'device': 'vscode测试环境'
    }}

session = requests.session()
data =  {'type': 'login', 'pwd': '123456'}

print(session.post('https://talktalk-six.vercel.app/api/v1/talktalk', json = data).json())

data =  {'type': 'send', 'data': {
        'text': '测试4',
        'device': 'vscode测试环境'
    }}
print(session.post('https://talktalk-six.vercel.app/api/v1/talktalk', json = data).json())
# print(requests.post('https://talktalk-six.vercel.app/api/v1/talktalk', json = data).json())