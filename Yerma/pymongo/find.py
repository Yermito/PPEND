import pymongo

myclient = pymongo.MongoClient('localhost:27017')
mydatabase = myclient["university"]
mycollection = mydatabase["faculty"]

for x in mycollection.find():
  print(x)
