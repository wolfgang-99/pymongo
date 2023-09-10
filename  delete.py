from pymongo import MongoClient
from bson import ObjectId
import pprint

MONGO_URL = r"mongodb+srv://wolfgang:SeBssfYUtkZs2hpr@cluster0.06gzzsk.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URL)
db = client.bank
acc_collection = db.account

## filter of the doc to delete
#doc_to_delete = {"_id":ObjectId('63fda895a911264ca583bd8f')}
#
## printing original doc
#pprint.pprint(acc_collection.find_one(doc_to_delete))
#
##expression that delete docs
#result =db.account.delete_one(doc_to_delete)
#
##search for docs after delete
#print("searching for target docs after delete")
#pprint.pprint(acc_collection.find_one(doc_to_delete))

#print("Docs deleted:"+str(result.deleted_count))
#

#--------------------------- using delete many method ---------------------#
## filter of the docs to delete
doc_to_delete={"balance":{"$lt":200}}

# search for sample doc before delete
pprint.pprint(acc_collection.find_one(doc_to_delete))

#expression that delete docs
result =db.account.delete_many(doc_to_delete)

#search for sample doc after delete
print("searching for target docs after delete")
pprint.pprint(acc_collection.find_one(doc_to_delete))

print("Docs deleted:"+str(result.deleted_count))


client.close()
