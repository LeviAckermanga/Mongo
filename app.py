from flask import Flask, render_template, request, jsonify, send_from_directory
from pymongo import MongoClient
from bson import ObjectId  
import os

#from config import MONGO_URI, SECRET_KEY

mongo_url = os.environ.get('MONGO_URL')

app = Flask(__name__)
#app.config['MONGO_URI'] = MONGO_URI
#app.config['SECRET_KEY'] = SECRET_KEY

#mongo_uri = app.config['MONGO_URI']
client = MongoClient(mongo_url)
db = client.data
collection = db.personas

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addPerson', methods=['POST'])
def add_person():
    data = request.get_json()
    collection.insert_one(data)
    return jsonify({"message": "Persona agregada exitosamente"})

@app.route('/getPeople')
def get_people():
    people = list(collection.find())
    for person in people:
        person['_id'] = str(person['_id'])
    return jsonify(people)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    