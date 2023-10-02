from config import MONGO_URI, SECRET_KEY
from pymongo import MongoClient


client = MongoClient(MONGO_URI)

db = client.data 

collection = db.personas  

# new_doc = {"name": "", "email": "", "age": ""}
# collection.insert_one(new_doc)

cursor = collection.find()
for document in cursor:
    print(document)

client.close()

print("Clave secreta:", SECRET_KEY)