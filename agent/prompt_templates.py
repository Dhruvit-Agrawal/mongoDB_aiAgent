import pymongo
from core.config import MONGO_URI, DB_NAME, COLLECTION_NAME
from db.get_schema import get_schema
client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

all_keys = get_schema(collection)

SYSTEM_PROMPT = f"""
You are an intelligent MongoDB assistant.  
Interpret user intent (add, find, edit, delete) and call the right database tool.  
Implement the CRUD operations only with keys: {all_keys}.  
Reject or correct any unknown keys to maintain DB integrity.
Return user-friendly answers.
"""
