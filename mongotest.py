import pymongo
client = pymongo.MongoClient("mongodb+srv://Jaydeep:q8gJygcT@ovs.gnpbd.mongodb.net/ovs?retryWrites=true&w=majority")
mycollection=client.ovs.voters_list
mycollection1=client.ovs.candidate_list
print(mycollection)
#mycollection.insert_one({"name":"jaydeep"})
#mycollection1.insert_one({"name":"jaydeep singh"})
for i in mycollection.find():
    print(i['name'])
for j in mycollection1.find():
    print(j['name'])
