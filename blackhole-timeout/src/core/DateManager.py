from src.entity_models.models import DateAddNewUsers
from bson.objectid import ObjectId
from typing import List
from datetime import datetime


class DateManager:

    def __init__(self, dao_factory):
        self.dao_factory = dao_factory
        self.dao_date = self.dao_factory.get_dao_date()

    def get_date(self):
        return self.dao_date.get_date()

    def update_date(self):
        date = DateAddNewUsers(
            month=datetime.utcnow().month,
            years=datetime.utcnow().year,
            datetime=datetime.utcnow()
        )
        return self.dao_date.update_date(date)
