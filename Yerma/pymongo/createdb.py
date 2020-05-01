import pymongo
myclient = pymongo.MongoClient('localhost:27017y')
mydatabase = myclient["university"]
dblist= myclient.list_database_names()
print(dblist )
#database created

#check for specific databse
if "university" in dblist:
  print("The database exists.")
