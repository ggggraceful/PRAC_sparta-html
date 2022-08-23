from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.gfgawqe.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

# 저장 - 예시
# 'name':'bobby','age':21  추가
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
# 'name':'bobby' 찾기(조건 있음)
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# {}  조건 없음
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
# 'name':'bobby'의 조건 'age':19 로 변경
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
# 'name':'bobby' 항목 삭제
db.users.delete_one({'name':'bobby'})