import pymongo
client = pymongo.MongoClient("mongodb+srv://dbjd:dbjd@clustertest.n1w7h.mongodb.net/dbsaud?retryWrites=true&w=majority")
db = client.test
mydatabase = client.dbsaud
test = { "abc":"pqr"}
rec = mydatabase.static.insert_one(test)
