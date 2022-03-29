import pymongo, json

from bson.objectid import ObjectId
from src.entity_models.models import User
from logger import logger as logger_main


logger = logger_main.getChild(__name__)

class DaoUser:

    def __init__(self, db):
        self.db = db
        self.coll = self.db.students

    # def add_users(self, users:List[User]):
    #     return self.coll.insert_many(users.dict(by_alias=True)).inserted_ids

    def add_user(self, user:User):
        return self.coll.insert_one(user.dict(by_alias=True)).inserted_id

    def get_users_blackhole(self, limite=10, blackhole=30):
        q = {"days_left": { '$gt' :  0, '$lt' : blackhole}}
        results = self.coll.find(q).sort("days_left", pymongo.ASCENDING).limit(limite)
        return [User.parse_obj(obj) for obj in results]



# def get_policies(self, orgId: str, pageSize: int, pageNumber: int):
#         q = {"org_id": ObjectId(orgId)}
#         results = self.coll.find(q)
#         if pageSize is not None and pageNumber is not None:
#             results = results.sort([("_id", pymongo.DESCENDING)]).skip(
#                 pageNumber*pageSize).limit(pageSize)
#         count = results.count(with_limit_and_skip=False)
#         return [Policy.parse_obj(obj) for obj in results], count
