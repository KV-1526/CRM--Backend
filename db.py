import os
from pymongo import MongoClient

mongo_url = os.getenv("MONGO_URL")

if not mongo_url:
    raise Exception("❌ MONGO_URL not found")

client = MongoClient(mongo_url)
db = client["crm_db"]
collection = db["interactions"]
