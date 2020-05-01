import pymongo

myclient = pymongo.MongoClient('localhost:27017')
mydatabase= myclient["university"]
mycollection = mydatabase["fit"]

mydict = { "name": "Tolkyn", "surname": "Zhagypar", "faculty":"IT" }

x = mycollection.insert_one(mydict)
