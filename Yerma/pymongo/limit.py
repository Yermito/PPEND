import pymongo

myclient = pymongo.MongoClient('localhost:27017')
mydatabase = myclient["university"]
mycollection = mydatabase["faculty"]

myresult = mycollection.find().limit(5)

#print the result:
for x in myresult:
  print(x)
