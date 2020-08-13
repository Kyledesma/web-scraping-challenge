from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape


app = Flask(__name__)


mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


@app.route('/')
def index():
    mars = mongo.db.mars_db.find_one()
    return render_template('index.html', mars=mars)


@app.route('/scrape')
def scrape():
    mars = mongo.db.mars_db
    data = mars_scrape.scrape()
    mars.update(
        {},
        data,
        upsert=True
    )
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
