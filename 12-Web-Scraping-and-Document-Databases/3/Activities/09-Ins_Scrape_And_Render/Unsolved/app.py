from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo 

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/craigslist_db'
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html', listing=listing)


@app.route('/scrape')
def scrape():
    executable_path = { 'executable_path': '/usr/local/bin/chromedriver'}
    

    url = "https://newyork.craigslist.org/d/free-stuff/search/zip"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find('a', class_='result-title').text
    price = soup.find('span', class_='result-price').text
    image = soup.find('img')['src']

    browser.quit()

    listing = {
        'title': title,
        'price': price,
        'image': image
    }

    mongo.db.listings.update({}, listing, upsert=True)

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)