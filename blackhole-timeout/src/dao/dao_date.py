from src.entity_models.models import DateAddNewUsers
from src.logger.logger import logger as logger_main

class DaoDate:

    def __init__(self, db):
        self.db = db
        self.coll = self.db.add_new_users

    def get_date(self):
        results = self.coll.find_one()
        if results is not None:
            return DateAddNewUsers.parse_obj(results)
        return results

    def update_date(self, date:DateAddNewUsers = None):
        results = self.coll.find_one()
        if results is not None:
            return self.coll.update_one({}, {"$set": date.dict(by_alias=True, exclude={'id'})})
        return self.coll.insert_one(date.dict(by_alias=True)).inserted_id
