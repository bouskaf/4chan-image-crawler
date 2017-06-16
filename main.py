from pymongo import MongoClient
import pprint
import json

client = MongoClient('mongodb://bouskfil:hesloheslo@apka-shard-00-00-hkdto.mongodb.net:27017,apka-shard-00-01-hkdto.mongodb.net:27017,apka-shard-00-02-hkdto.mongodb.net:27017/fapka?ssl=true&replicaSet=apka-shard-0&authSource=admin')

db = client.fapka
images = db.images


with open('res.json') as json_data:
    d = json.load(json_data)
    '''
    for href in d:
        image = {
            "url": href["href"]
        }
        #images.insert_one(image)

    '''
    print(d)
    images.insert_many(d)

#images.insert_one(image)
#images.insert_one(image)

#images.delete_many({})


cursor = images.find()

for document in cursor:
    print(document)
    print 'pepa z depa'

