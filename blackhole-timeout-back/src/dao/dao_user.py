import pymongo, json

from typing import List
from bson.objectid import ObjectId
from src.entity_models.models import User
from src.logger.logger import logger as logger_main

logger = logger_main.getChild(__name__)

class DaoUser:

    def __init__(self, db):
        self.db = db
        self.coll = self.db.students

    def add_users(self, users:List[User]):
        return self.coll.insert_many(users.dict(by_alias=True)).inserted_ids

    def add_user(self, user:User):
        q = {"user_id": user.user_id}
        if self.coll.find_one(q) is not None:
            logger.debug(f'User {user.user_id} already exist')
            return self.coll.update_one(q, {"$set": user.dict(by_alias=True, exclude={'id'})})
        return self.coll.insert_one(user.dict(by_alias=True)).inserted_id

    def get_users_blackhole(self, page_number: int, page_size: int, blackhole: int):
        q = {"days_left": { '$gt' :  0, '$lt' : blackhole}}
        results = self.coll.find(q)
        if page_size is not None and page_number is not None:
            results = results.sort([("days_left", pymongo.ASCENDING)]).skip(
                page_number*page_size).limit(page_size)
        return [User.parse_obj(obj) for obj in results]

    def get_users(self):
        results = self.coll.find()
        if results:
            return [user['user_id'] for user in results]
        return results

    def get_user(self, user_id:int):
        q = {"user_id": user_id}
        results = self.coll.find_one(q)
        logger.debug(results)
        if results:
            return User.parse_obj(results)
        return results

    def delete_user(self, user_id:int):
        q = {"user_id": user_id}
        return self.coll.delete_one(q)
