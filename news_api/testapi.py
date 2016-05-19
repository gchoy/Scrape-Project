import json
import pymongo
import bottle

from bson.json_util import dumps

MONGODB_URI = "mongodb://username:passwd@compose.io.com:port/theguardian?ssl=true&ssl_ca_certs=/path/to/mypem.pem"
MONGODB_DB = "theguardian"
MONGODB_COLLECTION = "newsarticles"

connection = pymongo.MongoClient(MONGODB_URI)

db = connection[MONGODB_DB]
collection = db[MONGODB_COLLECTION]

@bottle.route("/")
def index():
    return bottle.template('main')
   
    
@bottle.post('/search')
def search():
    
    key = bottle.request.forms.get("keyword")
    if key == None or key == "":
        key = "No matches"
    
    results = collection.find(  {'$or':[
            {'date':{'$regex':key, '$options':'i'}},
            {'author':{'$regex':key, '$options':'i'}},
            {'title':{'$regex':key, '$options':'i'}},
            {'content':{'$regex':key, '$options':'i'}},
            {'url':{'$regex':key, '$options':'i'}} 
                        ]})
    
    
    counts = results.count() 
    
    return bottle.template('result', {"counts": counts,"results":dumps(results)})         

     

bottle.run(host='localhost', port=8080)
   
