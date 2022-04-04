from bson.objectid import ObjectId
from typing import List
from datetime import datetime
from src.entity_models.models import DateAddNewUsers
from src.logger.logger import logger as logger_main

logger = logger_main.getChild(__name__)

class DateManager:

    def __init__(self, dao_factory):
        self.dao_factory = dao_factory
        self.dao_date = self.dao_factory.get_dao_date()

    def get_date(self):
        return self.dao_date.get_date()

    def update_date(self):
        date = datetime(datetime.utcnow().year + 1, 11, 1, 0, 0, 0)
        next_update_date = DateAddNewUsers(
            id=ObjectId(),
            month=date.month,
            years=date.year,
            datetime=date
        )
        return self.dao_date.update_date(next_update_date)
