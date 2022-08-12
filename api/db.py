import pymongo
import os



modburl = os.getenv('MONGODB_URL')
print('连接数据库:'+str(modburl))


client = pymongo.MongoClient(modburl)

db = client['test']

if __name__ == '__main__':
    # db.说说.update_one( {"时间": 1660264349.1976717}, {"$set":{"时间":"2022/08/12 08:52"}} )
    pass


