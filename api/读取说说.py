from bson.objectid import ObjectId
from db import db
def main(info):
    print('开始读取说说')
    data = list(db.说说.find())
    print('说说数据：' + str(data))
    jsondata = []
    for i in data:
        内容 = i['text']
        时间 = i['time']
        设备 = i['device']
        ip数据 = i['ip_data']
        说说id = str(i['_id'])
        json临时数据 = {"id": 说说id, "device": 设备, "time": 时间, "text": 内容, "ip_data": ip数据}
        jsondata.append(json临时数据)
    print(jsondata)
    return jsondata
if __name__ == '__main__':
    main('sb')