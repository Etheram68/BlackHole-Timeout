import json
from logger.logger import logger as logger_main


logger = logger_main.getChild(__name__)

class DaoUser:

    def __init__(self, db, con):
        self.db = db
        self.con = con

    def add_user(self, users):

        self.db.execute('''INSERT or REPLACE INTO user(userId, login, url,
                            imageUrl, blackHoleAt, daysLeft) VALUES(?, ?, ?, ?, ?, ?)''', \
                           (users.user_id, users.login, users.url, users.image_url, \
                            users.black_hole_at, users.days_left))
        self.con.commit()

    def get_users(self, cursor='', limite=10):
        self.db.execute(f'''SELECT userId, login, imageUrl, blackHoleAt
                            FROM user WHERE daysLeft <= 30 and login > '{cursor}' LIMIT {str(limite)}''')
        res = self.db.fetchall()
        return json.loads(json.dumps(res))
