# database/mongo_client.py

from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["alarm_ai_db"]  # Database
alarms_collection = db["alarms"]  # Collection to store alarms

# Optional: function to test connection
def test_connection():
    try:
        client.admin.command("ping")
        print("✅ Connected to MongoDB!")
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
