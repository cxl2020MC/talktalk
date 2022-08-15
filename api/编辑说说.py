from db import db
from bson.objectid import ObjectId

def main(info):
    print('开始编辑说说')
    id = info.get('id')
    data = info.get('data')
    print('要编辑的说说id: {}'.format(id))
    print('更新的数据库内容: {}'.format(data))
    if not id:
        print('未指定说说id')
        raise Exception('未指定说说id')
    if not data:
        print('未指定修改的data')
        raise Exception('未指定修改的data')
    print('开始更新数据库')
    db.说说.update_one({'_id': ObjectId(id)}, {'$set': data})
    print('数据库更新成功')

if __name__ == '__main__':
    main({'id': '62f8ff18ddf07289c571ed5b', 'data': {'text': '测试4修改'}})