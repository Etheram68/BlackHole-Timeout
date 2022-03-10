import sqlite3
from datetime import datetime
from dao.dao_user import DaoUser
from dao.dao_update import DaoUpdate

class DaoFactory:

    def __init__(self):
        self.con = sqlite3.connect('./BlackHole-Timeout.db')
        self.db = self.con.cursor()
        self.db.execute('''SELECT count(*) from sqlite_master
                                WHERE type='table' AND name='role' ''')
        rows = self.cur.fetchall()
        if not rows[0][0]:
            self.__init_tables__()

        self.dao_user = DaoUser(db=self.db, con=self.con)
        self.dao_update = DaoUpdate(db=self.db, con=self.con)


    def __init_tables__(self):
        self.db.execute('''CREATE TABLE IF NOT EXISTS update
                (date str)''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS user
                (userId str, login str, url str, imageUrl str, blackHoleAt str)''')
        self.con.commit()
        date = datetime.date(datetime.now().year, 11, 1, 0, 0, 0)
        self.db.execute("INSERT INTO guild VALUES(?)", (date))


    def get_dao_user(self):
        return self.dao_user

    def get_dao_update(self):
        return self.dao_update
