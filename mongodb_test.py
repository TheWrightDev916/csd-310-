import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.h2lbk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";

client = MongoClient(url)

db = client.pytech

print(db.list_collection_names)