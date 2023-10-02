from pymongo import MongoClient

mongo_uri = "mongodb+srv://LeviAckerman:2MtDBdH6G8GLuLIR@cluster1.an9fxsr.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(mongo_uri)

db = client.data 

collection = db.personas  

# new_doc = {"name": "", "email": "", "age": ""}
# collection.insert_one(new_doc)

cursor = collection.find()
for document in cursor:
    print(document)

client.close()