class DaoUser:

    def __init__(self, db, con):
        self.db = db
        self.con = con

    def add_user(self, users):

        self.db.execute("INSERT or REPLACE INTO user(userId, login, url, imageUrl, blackHoleAt) VALUES(?, ?, ?, ?, ?)", \
                (users.user_id, users.login, users.url, users.image_url, users.black_hole_at))
        self.con.commit()
