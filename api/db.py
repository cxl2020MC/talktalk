import pymongo

modburl = 'mongodb+srv://cxl2020mc:Qq365538151@cluster0.mjniqwk.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(modburl)

db = client['test']

if __name__ == '__main__':
    # db.说说.update_one( {"时间": 1660264349.1976717}, {"$set":{"时间":"2022/08/12 08:52"}} )
    pass


