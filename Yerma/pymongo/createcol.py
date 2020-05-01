import pymongo

myclient = pymongo.MongoClient('localhost:27017')

mydatabase = myclient["university"]

mycollection = mydatabase["fit"]

print(mydatabase.list_collection_names())
