from datetime import datetime


class DaoDate:

    def __init__(self, db):
        self.db = db

    def get_date(self):
        self.db.execute("SELECT * FROM date")
        res = self.db.fetchall()
        return res

    def update_date(self):
        date = datetime.date(datetime.now().year + 1, 11, 1, 0, 0, 0)
        self.db.execute("UPDATE date SET date=?", (date,))
        self.con.commit()
