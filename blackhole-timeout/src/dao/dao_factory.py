import pymongo, os

from pymongo import MongoClient

from src.dao.dao_user import DaoUser
from src.dao.dao_date import DaoDate
from logger import logger as logger_main


logger = logger_main.getChild(__name__)

class DaoFactory:

    def __init__(self):
        self.hostname = os.environ.get('MONGODB_HOSTNAME', 'localhost')
        self.port = os.environ.get('MONGODB_PORT', '27017')
        self.username = os.environ.get('MONGODB_ADMINUSERNAME', 'admin')
        self.password = os.environ.get('MONGODB_ADMINPASSWORD', "")

        try:
            client = MongoClient('mongodb://' + self.username + ':' + self.password + '@' + self.hostname + ':'+self.port)
            logger.info("Connected to MongoDB host: {}".format(self.hostname))
            logger.debug(client.server_info())
        except pymongo.errors.ServerSelectionTimeoutError as err:
            logger.error(err)

        self.db_api = client[os.environ.get('DATABASE_PREFIX', "_") + os.environ.get('MONGODB_DATABASE', "bag_")]
        self.db_log = client[os.environ.get('DATABASE_PREFIX', "_") + os.environ.get('MONGODB_DATABASE_LOGS_ORG', "logs_org")]

        self.dao_user = DaoUser(db=self.db_api)
        self.dao_date = DaoDate(db=self.db_api)


    def get_dao_user(self):
        return self.dao_user

    def get_dao_date(self):
        return self.dao_date
