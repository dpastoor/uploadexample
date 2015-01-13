import pymongo
from pymongo import MongoClient
connection = MongoClient('localhost', 3001)
# connect via database name
db = connection.meteor
# get collection from database
upload = db['cfs.uploads.filerecord']
print(upload.find_one()['copies']['uploads']['name'])


