from db import db
from flask import session
try:
    from api import tool
except:
    import tool

def main(info, ip):
    print('发送说说')
    if not session.get('login'):
        print('用户未登录，返回错误信息')
        raise Exception('未登录')
    else:
        print('用户已登录，开始发送说说')
    
    data = info['data']

    内容 = data['text']
    设备 = data['device']
    时间 = tool.格式化当前时间()
    ip信息 = tool.获取ip地址信息(ip)
    data = {
        'text': 内容,
        'time': 时间,
        'device': 设备,
        'ip_data': ip信息,
        'ip': ip
    }
    print('写入数据库:{}'.format(data))
    db.说说.insert_one(data)
    print('写入数据库成功')

if __name__ == '__main__':
    main({'data': {'text': '测试3', 'device': 'vscode测试环境'}}, '42.192.189.61')