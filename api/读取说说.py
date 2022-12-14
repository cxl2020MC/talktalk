from bson.objectid import ObjectId
from db import db
import pymongo


def main(info):
    print('开始读取说说')
    # 单次查询
    try:
        单次查询数量 = int(info.get('num'))
        if 单次查询数量 == None:
            print('未指定单次查询数量,使用默认数量.')
            单次查询数量 = 15
    except:
        print('获取单次查询数量失败,使用默认数量.')
        单次查询数量 = 15
    # 单次跳过
    try:
        单次跳过数量 = int(info.get('skip'))
        if 单次跳过数量 == None:
            print('未指定单次跳过数量,使用默认数量.')
            单次跳过数量 = 0
    except:
        print('获取单次跳过数量失败,使用默认数量.')
        单次跳过数量 = 0
    data = list(db.说说.find().limit(单次查询数量).skip(单次跳过数量).sort([("_id", pymongo.DESCENDING)]))
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