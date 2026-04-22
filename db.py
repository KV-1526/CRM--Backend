import os
from pymongo import MongoClient

client = MongoClient(os.getenv("mongodb+srv://kvgowtham03_db_user:zist9OkflgHPNNKq@cluster3.cfy8zii.mongodb.net/?appName=Cluster3"))
db = client["crm_db"]
collection = db["interactions"]