import pymongo

myclient = pymongo.MongoClient('localhost:27017')
mydatabase= myclient["university"]
mycollection = mydatabase["faculty"]


mycollection.drop()

#The drop() method returns true if the collection was dropped successfully, and false if the collection does not exist.
