import pymongo
from pymongo import MongoClient
connection = MongoClient()
print(connection.list_database_names())
