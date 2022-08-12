from bson.objectid import ObjectId
from db import db
def main(info):
    print('开始读取说说')
    data = list(db.说说.find())
    print('说说数据：' + str(data))
    jsondata = []
    for i in data:
        内容 = i['内容']
        时间 = i['时间']
        设备 = i['设备']
        说说id = str(i['_id'])
        json临时数据 = {"id": 说说id, "device": 设备, "time": 时间, "text": 内容}
        jsondata.append(json临时数据)
    print(jsondata)
    return jsondata
if __name__ == '__main__':
    main('sb')