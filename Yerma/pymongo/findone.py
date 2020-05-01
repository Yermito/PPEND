import pymongo

myclient = pymongo.MongoClient('localhost:27017')
mydatabase = myclient["university"]
mycollection = mydatabase["faculty"]
x = mycollection.find_one()
#finds first inserted object
print(x)
