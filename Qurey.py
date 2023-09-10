from bson import ObjectId
from pymongo import MongoClient
import pprint

MONGO_URL = r"mongodb+srv://wolfgang:SeBssfYUtkZs2hpr@cluster0.06gzzsk.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URL)

db = client.bank
acont_collection = db.account

## find method with object id
#doc_to_find = {"_id":ObjectId('63fda8f8323472df0c58b5c2')}

## find method with other parament
doc_to_find = {"balance":{"$gt":4000}}

result = acont_collection.find(doc_to_find)

for doc in result:
    pprint.pprint(doc)
    print()
client.close()