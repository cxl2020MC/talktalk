from db import db
from bson.objectid import ObjectId

def main(info):
    print('开始点赞说说')
    id = info.get('id')
    print('要编辑的说说id: {}'.format(id))
    if not id:
        print('未指定说说id')
        raise Exception('未指定说说id')
    print('开始更新数据库')
    db.说说.update_one({'_id': ObjectId(id)}, {'$inc': 1})
    print('数据库更新成功')