from pymongo import MongoClient

client=MongoClient()

coffees_collection=client.db.coffee