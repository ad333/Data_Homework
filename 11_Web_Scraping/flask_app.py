from flask import Flask, render_template, jsonify
import pymongo
import scrape_mars
import pprint

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db
collection = db.mars_collection


@app.route('/')
def home():
    mars_data = list(db.collection.find())
    return render_template('index.html', mars_data = mars_data)


@app.route('/scrape')
def scrape():
    mars_data = scrape_mars.scrape()
    collection.update(
        {},
        mars_data,
        upsert=True
    )
    # collection.insert_one(mars)
    return "scrape successfull"   

if __name__ == "__main__":
    app.run(debug=True)