import pymongo
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME=os.getenv("DB_NAME")
COLLECTION_NAME=os.getenv("COLLECTION_NAME")

client = pymongo.MongoClient(MONGO_URI)

# Connect to MongoDB

db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def get_schema(collection):
    pipeline = [
        {"$project": {"arrayofkeyvalue": {"$objectToArray": "$$ROOT"}}},
        {"$unwind": "$arrayofkeyvalue"},
        {"$group": {"_id": None, "allKeys": {"$addToSet": "$arrayofkeyvalue.k"}}},
        {"$project": {"_id": 0, "allKeys": 1}}  # Optional: clean output format
    ]
    schema_cursor = collection.aggregate(pipeline)
    schema_list = list(schema_cursor)  # iterate cursor fully
    if schema_list and "allKeys" in schema_list[0]:
        all_keys = schema_list[0]["allKeys"]
        print("Schema keys:", all_keys)
        return all_keys
    else:
        print("No schema keys found.")
        return []



