from db import db
from api import tool

def main(info, ip):
    print('发送说说')
    data = info['data']
    内容 = info['text']
    设备 = info['device']
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