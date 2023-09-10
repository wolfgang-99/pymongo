import pprint
from pymongo import MongoClient

MONGO_URL = r"mongodb+srv://wolfgang:SeBssfYUtkZs2hpr@cluster0.06gzzsk.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URL)

# to get refrence to the "bank"database
db = client.bank

# to get refrence to "account" collection
acc_collection = db.account

# OPREATION to be carried out (claculate the avegrage balance of saving and checking account with balance of greater than 1000)

# selsect accounts with balance of greater than $1000
match_by_balance = {"$match": {"balance": {"$gt": 1000}}}

# seprate docs by acc type and calcculate the average balance for each acc type.
group_by_account_calculate_avg_balance = {
    "$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}
}

# create an aggregation pipline using "stage_match_balance" and "stage_group_account_type"
pipeline = [
    match_by_balance,
    group_by_account_calculate_avg_balance,
]

# perform an aggregation on "pipline"
results = acc_collection.aggregate(pipeline)

print(
    "Average balance of checking and saving accounts with balance greater than $1000:" "\n"
)
for item in results:
    pprint.pprint(item)

client.close()
