import pymongo, json

from bson.objectid import ObjectId
from entity_models.models import User
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

