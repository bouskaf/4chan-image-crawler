from pymongo import MongoClient
import pprint
import json

# client = MongoClient('mongodb://bouskfil:hesloheslo@apka-shard-00-00-hkdto.mongodb.net:27017,apka-shard-00-01-hkdto.mongodb.net:27017,apka-shard-00-02-hkdto.mongodb.net:27017/fapka?ssl=true&replicaSet=apka-shard-0&authSource=admin')
#

client = MongoClient('localhost', 27017)
db = client['4chan']
posts = db.posts

# posts.delete_many({})
cursor = posts.find()

for document in cursor:
    print(document)

#
# with open('idnesarticle.json') as json_data:
#     d = json.load(json_data)
#     '''
#     for href in d:
#         image = {
#             "url": href["href"]
#         }
#         #images.insert_one(image)
#
#     '''
#     print(d)
#     #catalog.insert_many(d)
#     # images.insert_many(d)
#
# #images.insert_one(image)
# #images.insert_one(image)
#
# #images.delete_many({})
#
#
# cursor = catalog.find()
#
# for document in cursor:
#     print(document)
#
#
#
#


from bs4 import BeautifulSoup

# with open('idnesarticle.json') as json_data:
#     d = json.load(json_data)
#     '''
#     for href in d:
#         image = {
#             "url": href["href"]
#         }
#         #images.insert_one(image)
#