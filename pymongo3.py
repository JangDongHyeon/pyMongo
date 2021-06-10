from bs4 import BeautifulSoup
import requests
import pymongo
import re

conn = pymongo.MongoClient()
actor_db = conn.cine21
actor = actor_db.actor_collection

# actor_collection.find_one({})
# docs = actor_collection.find({}).limit(3)
# # for doc in docs:
# # print(doc)
# actor = actor_collection

# actor.create_index('배우이름')

# actor.index_information()

# actor.drop_indexes()

# actor.create_index('배우이름')

# actor.create_index('랭킹')

# actor.create_index('흥행지수')

# print(actor.index_information())


# actor.drop_indexes()
# actor.create_index([('직업', 'text')])

# actor.index_information()

# docs = actor.find({'$text': {'$search': '가수'}})
# for doc in docs:
#     print(doc)


actor.drop_indexes()

actor.create_index(
    [('출연영화', pymongo.TEXT), ('직업', pymongo.TEXT), ('흥행지수', pymongo.DESCENDING)])
docs = actor.find({'$text': {'$search': '신과'}})
for doc in docs:
    print(doc)
