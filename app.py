from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars_db'
mongo = PyMongo(app)


@app.route("/")
def index():
    mars_scrape_data = mongo.db.mars_scrape_data.find_one()
    return render_template("index.html", mars_scrape_data=mars_scrape_data)

@app.route("/scrape")
def scrape():
    mars_scrape_data = scrape_mars.scrape()

    mongdo.db.mars_scrape_data.update({}, mars_scrape_data, upsert=True)
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)