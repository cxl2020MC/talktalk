import pymongo

modburl = 'mongodb+srv://cxl2020mc:Qq365538151@cluster0.mjniqwk.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(modburl)

db = client['test']

if __name__ == '__main__':
    import time
    databases = client.list_database_names()
    print('共有数据库：' + str(databases))
    collections = db.list_collection_names()
    print('共有集合：' + str(collections))
    # data = {
        # '内容': '测试测试',
        # '时间': time.time(),
        # '设备': 'vscode测试'
    # }
    # db.说说.insert_one(data)

    result = db.说说.find()
    comment = list(result)
    print(comment)
