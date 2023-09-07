from flask import Flask, render_template, request, jsonify, send_from_directory
from pymongo import MongoClient
from bson import ObjectId  
import os

app = Flask(__name__)

mongo_uri = "mongodb+srv://LeviAckerman:2MtDBdH6G8GLuLIR@cluster1.an9fxsr.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)
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
    app.run(debug=True)
    