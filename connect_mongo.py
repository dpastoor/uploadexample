import pymongo
from pymongo import MongoClient
connection = MongoClient('localhost', 3001)
# connect via database name
db = connection.meteor
# get collection from database
upload = db['cfs.uploads.filerecord']
print(upload.find_one()['copies']['uploads']['name'])
print(upload.find_one())

# try removing object
#upload.remove({"copies.uploads.name":"21-144_Ketek_BioPharmr_P1.pdf"})
upload.remove({}) # to clear out db
#upload.insert('')
# method of printing one
# notice to search for nested documents you use the `.` to search

#print(upload.find_one({'copies.uploads.name':'42684061.PDF'}))

#find returns cursor object so must iterator over it get actual info rather
# than cursor object
#for u in upload.find({"_id": "xcbvufwBLRvdwaf6Q"}):
#    print(u)

