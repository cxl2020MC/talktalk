from db import db
from bson.objectid import ObjectId

def main(info):
    print('开始删除说说')
    id = info.get('id')
    print('要删除的说说id: {}'.format(id))
    if not id:
        print('未指定说说id')
        raise Exception('未指定说说id')
    print('开始更新数据库')
    db.说说.delete_one({'_id': ObjectId(id)})
    print('数据库更新成功')

if __name__ == '__main__':
    main({'id': '62f6fb80a5b5809acc94afb8'})