

import pymongo


conn = pymongo.MongoClient()
actor_db = conn.cine21
actor = actor_db.actor_collection
elemmatch_sample = actor_db.sample
# elemmatch_sample.insert_many([
#     {'results': [82, 85, 88]},
#     {'results': [75, 88, 91]}
# ])
# actor_collection.find_one({})
# docs = actor_collection.find({}).limit(3)
# for doc in docs:
#     print(doc)
# actor = actor_collection


# docs = actor_collection.find({}).sort('생년월일', pymongo.DESCENDING).limit(10)
# for doc in docs:
#     print (doc)

# docs = actor.find({'특기': {'$exists': True}}).sort('흥행지수').limit(5)
# for doc in docs:
#     print(doc)

# docs = actor.find({'생년월일': {'$exists': False}}, {'배우이름': 1, '_id': 0})
# for doc in docs:
#     print(doc)

# docs = actor.find({'흥행지수': {'$gte': 1000}, '출연영화': '극한직업'},
#                   {'배우이름': 1, '출연영화': 1, '_id': 0})
# for doc in docs:
#     print(doc)

# docs = actor.find({'$or': [{'출연영화':'극한직업'}, {'출연영화':'더 킹'}] }, {'배우이름':1, '출연영화':1, '_id':0})
# for doc in docs:
#     print(doc)

# docs = actor.find({ '흥행지수': {'$gte': 10000}, '$or': [{'출연영화':'극한직업'}, {'출연영화':'더 킹'}] }, {'배우이름':1, '출연영화':1, '_id':0})
# for doc in docs:
#     print(doc)

# docs = actor.find({'$nor': [{'흥행지수': {'$gte': 10000}}, {'흥행지수': {'$lte': 2000}}]}, {
#                   '배우이름': 1, '흥행지수': 1, '_id': 0})
# for doc in docs:
#     print(doc)

# docs = actor.find({'흥행지수': {'$in': [9444, 9199]}}, {
#                   '배우이름': 1, '흥행지수': 1, '_id': 0})
# for doc in docs:
#     print(doc)

# docs = actor.find({'흥행지수': {'$nin': [9182, 8439]}}, {
#                   '배우이름': 1, '흥행지수': 1, '_id': 0}).limit(3)
# for doc in docs:
#     print(doc)

# docs = actor.find(
#     {'흥행지수': {'$nin': [9444, 9199]}, '흥행지수': {'$lt': 10000}}, {'배우이름': 1, '흥행지수': 1, '_id': 0}).limit(3)
# # docs = actor.find({'$nor': [{'흥행지수': {'$in': [9182, 8439]}}, {
# #                   '흥행지수': {'$gt': 10000}}]}, {'배우이름': 1, '흥행지수': 1, '_id': 0}).limit(3)
# for doc in docs:
#     print(doc)

# docs = actor.find({'출연영화': '극한직업'})
# for doc in docs:
#     print(doc)

# docs = actor.find({'$or': [{'출연영화': '극한직업'}, {'출연영화': '사바하'}]})
# for doc in docs:
#     print (doc)

# docs = actor.find({'출연영화': {'$all': ['변산', '사바하']}})
# for doc in docs:
#     print(doc)

# docs = actor.find({'출연영화.0': '사바하'})
# for doc in docs:
#     print(doc)

# docs = actor.find({'출연영화': {'$size': 5}})
# for doc in docs:
#     print(doc)

docs = elemmatch_sample.find({'results': {'$gte': 90, '$lt': 85}})
for doc in docs:
    print(doc)

docs = elemmatch_sample.find(
    {'results': {'$elemMatch': {'$gte': 75, '$lt': 80}}})
for doc in docs:
    print(doc)
