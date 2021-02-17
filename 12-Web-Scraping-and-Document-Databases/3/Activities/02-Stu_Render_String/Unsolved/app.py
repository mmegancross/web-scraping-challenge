# import necessary libraries
from flask import Flask, render_template
import pymongo

# @TODO: Initialize your Flask app here
app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.dataviz
collection = db.staff

name = 'Megan'
hobby = 'Baking'

staff = [
    {
        "name": "Michael",
        "role": "Instructor",
        "email": "michael@email.com"
    },
    {
        "name": "Brianna",
        "role": "TA",
        "email": "brianna@email.com"
    },
    {
        "name": "Taylor",
        "role": "TA",
        "email": "taylor@email.com"
    },
]

collection.drop()
collection.insert_many(staff)

# @TODO:  Create a route and view function that takes in a string and renders index.html template
# CODE GOES HERE
@app.route("/")
def index():
    return render_template("index.html", name=name, hobby=hobby)

@app.route("/bonus")
def bonus():
    return render_template("bonus.html", name=name, hobby=hobby)

if __name__ == "__main__":
    app.run(debug=True)
