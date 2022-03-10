from datetime import datetime


class DaoUpdate:

    def __init__(self, db, con):
        self.db = db
        self.con = con

    def get_date(self):
        self.db.execute("SELECT * FROM update")
        res = self.db.fetchall()
        return res

    def update_date(self):
        date = datetime.date(datetime.now().year + 1, 11, 1, 0, 0, 0)
        self.db.execute("UPDATE update SET date=?", (date,))
        self.con.commit()
