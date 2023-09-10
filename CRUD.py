from pymongo import MongoClient


MONGO_URL = r"mongodb+srv://wolfgang:SeBssfYUtkZs2hpr@cluster0.06gzzsk.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URL)


# step 1 Define the callback that specifies the sequence of operations to perform inside the transaction
def callback(session, transfer_id=None, account_id_recevier=None, account_id_sender=None, transfer_amount=None):
    # Get reference to "accounts" collection
    acc_collection = session.client.bank.accounts

    # Get reference to "transfer" collection
    transfers_collection = session.client.bank.transfers
    transfer = {
        "transfer_id": transfer_id,
        "to_account": account_id_recevier,
        "from_account": account_id_sender,
        "amount": {"$numberDecimal": transfer_amount},
    }

    # Transaction opreations
    # Important : you must pass the session to each opreation

    # update sender account : subtract amount from balance and add transfer ID
    acc_collection.update_one(
        {"account_id": account_id_sender},
        {
            "$inc": {"balance": -transfer_amount},
            "$push": {"transfer_complete": transfer_id}
        },
        session=session
    )

    # update receiver account : add amount to balance and add transfer ID
    acc_collection.update_one(
        {"account_id": account_id_recevier},
        {
            "$inc": {"balance": transfer_amount},
            "$push": {"transfer_complete": transfer_id}
        },
        session=session
    )

    # Add new transfer to "transfers" collection
    transfers_collection.insert_one(transfer, session=session)

    print("Transaction sucessful")

    return
def callback_wrapper(s):
    callback(
        s,
        transfer_id="TR2134567",
        account_id_recevier="MDB342345",
        account_id_sender="MDB568345",
        transfer_amount= 100,
    )

# start a client session , then start a transaction.
with client.start_session() as session:
    session.with_transaction(callback_wrapper)

client.close()