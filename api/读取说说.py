from bson.objectid import ObjectId
from db import db


def main(info):
    print('开始读取说说')
    单次查询数量 = info.get('num')
    data = list(db.说说.find().limit(15))
    print('说说数据: {}'.format(data))
    jsondata = []
    for i in data:
        内容 = i.get('text')
        时间 = i.get('time')
        设备 = i.get('device')
        ip数据 = i.get('ip_data')
        说说id = str(i['_id'])
        json临时数据 = {"id": 说说id, "device": 设备, "time": 时间, "text": 内容, "ip_data": ip数据}
        jsondata.append(json临时数据)
    # print(jsondata)
    return jsondata



if __name__ == '__main__':
    print(main('sb'))