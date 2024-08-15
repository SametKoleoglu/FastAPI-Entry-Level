from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

URI = os.getenv("MONGO_URI")


client = MongoClient(URI, server_api=ServerApi('1'))
db = client.FastAPIBlog
blogs_collection = db["blogs"]

try:
     client.admin.command('ping')
     print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
     print(e)