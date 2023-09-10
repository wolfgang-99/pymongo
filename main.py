from pymongo import MongoClient
import datetime

MONGO_URL = r"mongodb+srv://wolfgang:SeBssfYUtkZs2hpr@cluster0.06gzzsk.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URL)


# to get refrence to the "bank"database
db= client.bank

#to get refrence to "account" collection
acc_collection = db.account

# creating file/ or document

new_alert = [
#    {
#    "acc-name": "alex",
#    "acc-type": "check",
#    "balance": 78987654,
#    "last-update":datetime.datetime.utcnow()},
#    {"acc-name": "wolf ",
#    "acc-type": "check",
#    "balance": 56789854,
#    "last-update":datetime.datetime.utcnow()}
    {
        "account_id": "MDB234456543",
        "account_holder": "Wolf got",
        "account_type": "savings",
        "balance": {"$numberDecimal":"2045.23"},
        "transfers_complete": ["TR345563", "TR239045"],
        "last-update":datetime.datetime.utcnow()
    },
    {
        "account_id": "MDB234456544",
        "account_holder": "fish wot",
        "account_type": "savings",
        "balance": {"$numberDecimal": "1345.23"},
        "transfers_complete": ["TR345563", "TR239045"],
        "last-update":datetime.datetime.utcnow()
    },
    {
        "account_id": "MDB234456545",
        "account_holder": "Book Got",
        "account_type": "check",
        "balance": {"$numberDecimal": "2345.23"},
        "transfers_complete": ["TR345563", "TR239045"],
        "last-update":datetime.datetime.utcnow()
    },
    {
        "account_id": "MDB234456546",
        "account_holder": "Will Sand",
        "account_type": "check",
        "balance": {"$numberDecimal": "1045.23"},
        "transfers_complete": ["TR345864", "TR239145"],
        "last-update":datetime.datetime.utcnow()
    },
    {
        "account_id": "MDB234456547",
        "account_holder": "Mod got",
        "account_type": "check",
        "balance": {"$numberDecimal": "2345.23"},
        "transfers_complete": ["TR345564", "TR239145"],
        "last-update":datetime.datetime.utcnow()
    },
    {
        "account_id": "MDB234456548",
        "account_holder": "Alex lot",
        "account_type": "savings",
        "balance": {"$numberDecimal": "5005.23"},
        "transfers_complete": ["TR345563", "TR239045"],
        "last-update":datetime.datetime.utcnow()
    }
]

# to insert the document or file into the collection
result = acc_collection.insert_many(new_alert)

document_id =result.inserted_ids
print(f"no of doc added {len(document_id)}")
print(f"_id of inserted document: {document_id}")
client.close()