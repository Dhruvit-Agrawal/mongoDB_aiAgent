import pymongo
from core.config import MONGO_URI, DB_NAME, COLLECTION_NAME
from db.get_schema import get_schema
client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

schema = get_schema(collection)
