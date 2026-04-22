import os
from pymongo import MongoClient

mongo_url = os.getenv("MONGO_URL")

print("🔥 DEBUG MONGO_URL:", mongo_url)

if not mongo_url:
    raise Exception("❌ MONGO_URL not set")

try:
    client = MongoClient(mongo_url)
    db = client["crm_db"]
    collection = db["interactions"]
    print("✅ MongoDB connected successfully")
except Exception as e:
    print("❌ MongoDB connection failed:", e)
    raise e
