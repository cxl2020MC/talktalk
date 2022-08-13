from db import db
from api import tool

def main(info, ip):
    print('发送说说')
    data = info['data']
    内容 = data['text']
    时间 = tool.格式化当前时间()
    设备 = data['device']
    ip信息 = tool.获取ip地址信息(ip)
    data = {
        'text': 内容,
        'time': 时间,
        'device': 设备,
        'ip_data': ip信息
    }
    print('写入数据库,data:{}'.format(data))
    db.说说.insert_one(data)
    print('写入数据库成功')