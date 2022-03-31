from src.entity_models.models import User
from bson.objectid import ObjectId
from typing import List


class UserManager:

    def __init__(self, dao_factory):
        self.dao_factory = dao_factory
        self.dao_user = self.dao_factory.get_dao_user()

    def add_users(self, users: List[User]):
        return self.dao_user.add_users(users)

    def add_user(self, user: User):
        return self.dao_user.add_user(user)

    def get_users_blackhole(self, page_number: int, page_size: int=30, blackhole: int=30):
        return self.dao_user.get_users_blackhole(page_number, page_size, blackhole)

    def get_users(self):
        return self.dao_user.get_users()