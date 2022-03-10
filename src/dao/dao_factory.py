import sqlite3

class DaoFactory:

    def __init__(self):
        self.con = sqlite3.connect('./BlackHole-Timeout.db')
        self.cur = self.con.cursor()
        self.cur.execute('''SELECT count(*) from sqlite_master
                                WHERE type='table' AND name='role' ''')
        rows = self.cur.fetchall()
        if not rows[0][0]:
            self.__init_tables__()


    def __init_tables__(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS update
                (date str)''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS user
                (userId str, login str, url str, imageUrl str, blackHoleAt str)''')
        self.con.commit()
