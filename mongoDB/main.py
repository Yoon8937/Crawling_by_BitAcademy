# 몽고디비와 파이썬 연동
import pymongo

conn = pymongo.MongoClient()#연결
db = conn.bitDB #bitDB 데이터베이스 이름
users = db.users #컬렉션

#users에서 조회하기
users = users.find({}).limit(3)
for user in users:
    print(user)

#inventory에서 조회하기
inventory = db.inventory.find({}, {'_id':0})
for inv in inventory:
    print(inv)

newInvent = [{"item":"speaker", "qty":50, "size":{"h":22, "w":22, "uom":"cm"}, "status":"SS" }]
db.inventory.insert_many(newInvent)

db.inventory.update_many({"status:":"SS"}, {"$set":{"status":"P"}})


















