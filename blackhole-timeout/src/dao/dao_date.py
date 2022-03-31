from datetime import datetime
from unittest import result
from src.entity_models.models import DateAddNewUsers
from src.logger.logger import logger as logger_main

class DaoDate:

    def __init__(self, db):
        self.db = db
        self.coll = self.db.add_new_users

    def get_date(self):
        results = self.coll.find_one()
        print(results)
        if results is not None:
            return DateAddNewUsers.parse_obj(results)
        return results

    def update_date(self, date:DateAddNewUsers = None):
        q = {}
        results = self.coll.find(q)
        if results is not None:
            return self.coll.update_one(q, {"$set": date.dict(by_alias=True, exclude={'id'})})
        date = DateAddNewUsers(
            month=datetime.utcnow().month,
            years=datetime.utcnow().year,
            datetime=datetime.utcnow()
        )
        return self.coll.insert_one(date.dict(by_alias=True)).inserted_id
