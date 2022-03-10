import sqlite3
from datetime import datetime
from dao.dao_user import DaoUser
from dao.dao_date import DaoDate
from logger.logger import logger as logger_main


logger = logger_main.getChild(__name__)

class DaoFactory:

    def __init__(self):
        self.con = sqlite3.connect('./BlackHole-Timeout.db')
        self.db = self.con.cursor()
        self.db.execute('''SELECT count(*) from sqlite_master
                                WHERE type='table' AND name='user' ''')
        rows = self.db.fetchall()
        if not rows[0][0]:
            logger.debug("Init Table")
            self.__init_tables__()

        self.dao_user = DaoUser(db=self.db, con=self.con)
        self.dao_date = DaoDate(db=self.db, con=self.con)


    def __init_tables__(self):
        self.db.execute('''CREATE TABLE IF NOT EXISTS date
                (date str)''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS user
                (userId str, login str, url str, imageUrl str, blackHoleAt str)''')
        self.con.commit()
        new_date = datetime(int(datetime.now().year), 11, 1, 0, 0, 0)
        if datetime.now() > new_date:
            new_date = datetime(int(datetime.now().year + 1), 11, 1, 0, 0, 0)
        self.db.execute("INSERT INTO date VALUES(?)", (str(new_date),))
        self.con.commit()


    def get_dao_user(self):
        return self.dao_user

    def get_dao_date(self):
        return self.dao_date
