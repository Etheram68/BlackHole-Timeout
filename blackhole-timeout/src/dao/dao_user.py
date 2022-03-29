import pymongo, json

from bson.objectid import ObjectId
from logger.logger import logger as logger_main


logger = logger_main.getChild(__name__)

class DaoUser:

    def __init__(self, db, con):
        self.db = db
        self.coll = self.db.students

    def add_user(self, users):
        return self.coll.insert_many(users.dict(by_alias=True)).inserted_ids

