import pymongo

myclient = pymongo.MongoClient('localhost:27017')
mydatabase = myclient["university"]
mycollection = mydatabase["faculty"]

myquery = { "faculty": "IT" }

mycollection.delete_one(myquery)
