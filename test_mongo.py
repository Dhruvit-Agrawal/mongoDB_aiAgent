import pymongo
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME=os.getenv("DB_NAME")
COLLECTION_NAME=os.getenv("COLLECTION_NAME")

client = pymongo.MongoClient(MONGO_URI)
print("✅ Connected to MongoDB!")


db_list = client.list_database_names()
print("Available Databases:", db_list)

# Connect to MongoDB
db=client[DB_NAME]

collection = db[COLLECTION_NAME]

schema = collection.aggregate([
    {"$project": {"arrayofkeyvalue": {"$objectToArray": "$$ROOT"}}},
    {"$unwind": "$arrayofkeyvalue"},
    {"$group": {"_id": None, "allKeys": {"$addToSet": "$arrayofkeyvalue.k"}}}
])
print(((list(schema))[0]))

#uvicorn api.main_api:app --reload --host 0.0.0.0 --port 8000
