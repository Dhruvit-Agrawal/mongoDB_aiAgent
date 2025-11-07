from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DB_NAME = os.getenv("DB_NAME", "myTestDB")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "myFirstMDB")
