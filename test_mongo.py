import os
import sys
import json
import pymongo
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

# Load environment variables from .env file
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

# Check if MONGO_DB_URL is set
if not MONGO_DB_URL:
    raise ValueError("Error: MONGO_DB_URL is not set. Please check your .env file.")

# Create a new client and connect to the server
try:
    client = MongoClient(MONGO_DB_URL)
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error connecting to MongoDB:", e)