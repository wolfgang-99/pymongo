from pymongo import MongoClient
from bson import ObjectId
import pprint

MONGO_URL =r"mongodb+srv://wolfgang:SeBssfYUtkZs2hpr@cluster0.06gzzsk.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URL)
db = client.bank
acc_collection = db.account

## filter of the doc to update
doc_to_update = {"_id":ObjectId('63fda895a911264ca583bd8f')}

## printing original doc
#pprint.pprint(acc_collection.find_one(doc_to_update))

## update content
add_to_balance = {"$inc":{"balance": 100}}

## updating the doc
update = acc_collection.update_one(doc_to_update,add_to_balance)
## print updated doc
#pprint.pprint(acc_collection.find_one(doc_to_update))



#--------------------------- using update many method ---------------------#
## filter of the doc to update
doc_to_update = {"acc-type": "check"}

## contect to update
add_mini_balance = {"$set":{"minimul balance": 100}}

## updating the doc
update_doc = acc_collection.update_many(doc_to_update, add_mini_balance)

print("docments matched:"+ str(update_doc.matched_count))
print("docments matched:"+ str(update_doc.modified_count))
pprint.pprint(acc_collection.find_one(doc_to_update))

client.close()