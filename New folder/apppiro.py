from flask import Flask, jsonify, render_template
from pymongo import MongoClient
from bson.json_util import dumps
from flask_cors import CORS

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/StockData"
client = MongoClient(port=27017)
db = client['StockData']

@app.route('/stockinfo', methods=['GET'])
def get_stockinfo():
    data = db.StockInfo.find({})
    results = [result for result in data]
    return jsonify(results)  # Converts BSON to JSON

@app.route('/openclose', methods=['GET'])
def get_openclose():
    data = db.OpenClose.find({})
    results = [result for result in data]
    return jsonify(results)  # Converts BSON to JSON

@app.route('/highlow', methods=['GET'])
def get_highlow():
    data = db.HighLow.find({})
    results = [result for result in data]
    return jsonify(results)  # Converts BSON to JSON

@app.route('/volume', methods=['GET'])
def get_volume():
    data = db.Volume.find({}, {'_id':0})
    results = [result for result in data]
    return jsonify(results)  # Converts BSON to JSON

@app.route('/tradinginfo', methods=['GET'])
def get_tradinginfo():
    data = db.TradingInfo.find({}, {'_id':0})
    results = [result for result in data]
    return jsonify(results)  # Converts BSON to JSON

@app.route("/")
def main(): 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)




