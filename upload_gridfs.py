import pymongo
from pymongo import MongoClient
import gridfs
connection = MongoClient('localhost', 3001)
# connect via database name
db = connection.meteor
#fs=gridfs.GridFS(db) # how to create new fs
fs = gridfs.GridFS(db, collection = 'cfs_gridfs.pdfs')
data=open("/Users/devin/projectUploads/add.pdf", "rb")
read_data = data.read()
fs.put(read_data, filename="add.pdf")

filelist=fs.list()
print(filelist)

output=open("/Users/devin/Desktop/test.pdf", "wb")
output.write(read_data)
output.close()