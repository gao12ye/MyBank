from flask import Flask
import pymongo
from bson.json_util import loads, dumps 

app = Flask(__name__)
@app.route('/<byuser>')
def trans(byuser):
    results = col_transaction.find_one({"byuser": byuser})
    #return transaction.find_one({"byuser": byuser})
    #return results['byuser']
    return dumps(results)

if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb+srv://admin:Mongosummer01!@cluster0-slq91.mongodb.net/test?retryWrites=true&w=majority")
    db_mybank=client.mybank
    col_transaction=db_mybank.transaction
    app.run(host='127.0.0.1', port=8080, debug=True)

