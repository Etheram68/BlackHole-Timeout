from src.entity_models.models import DateAddNewUsers
from bson.objectid import ObjectId
from typing import List


class DateManager:

    def __init__(self, dao_factory):
        self.dao_factory = dao_factory
        self.dao_date = self.dao_factory.get_dao_date()

    def get_date(self):
        return self.dao_date.get_date()
