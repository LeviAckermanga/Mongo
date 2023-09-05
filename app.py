from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

mongo_uri = "mongodb+srv://LeviAckerman:2MtDBdH6G8GLuLIR@cluster1.an9fxsr.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)
db = client.data
collection = db.personas

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addPerson", methods=["POST"])
def add_person():
    data = request.get_json()
    collection.insert_one(data)
    return jsonify({"message": "Persona agregada exitosamente"})

@app.route("/getPeople")
def get_people():
    people = list(collection.find())
    return jsonify(people)

if __name__ == "__main__":
    app.run(debug=True)
