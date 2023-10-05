#from config import MONGO_URI, SECRET_KEY
from pymongo import MongoClient
import os 

mongo_url = os.environ.get('MONGO_URL')

if mongo_url is None:
    raise ValueError("La variable de entorno MONGO_URL no está configurada.")

client = MongoClient('MONGO_URL')

#client = MongoClient(MONGO_URI)

db = client.data 

collection = db.personas  

cursor = collection.find()
for document in cursor:
    print(document)

client.close()

