import requests, time
from logger.logger import logger as logger_main
from datetime import datetime

logger = logger_main.getChild(__name__)

class School42Client():

    def __init__(self, client_id, client_secret):
        self.site = "https://api.intra.42.fr"
        self.authorization_url = "/oauth/authorize"
        self.token_url = "/oauth/token"
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None
        self.expire = None


    def get_token(self):
        payload = {'grant_type': 'client_credentials', 'response_type': 'code'}

        r = requests.post(self.site+self.token_url,
                data=payload, auth=(self.client_id, self.client_secret))
        if r.status_code == 200:
            r = r.json()
            self.token = r['access_token']
            self.expire = r['expires_in']
            logger.info(f'New Token Created, expires in {self.expire} s')
        else:
            logger.error(f'Could not resolve {self.site+self.token_url}, returned error {r.status_code}')
        return self.token


    def get(self, root, data=None):
        logger.debug(f'Get url {self.site}{root} and data: {data}')
        retry_request = 0

        while True:
            headers = {'Authorization': f'Bearer {self.token}'}
            r = requests.get(f'{self.site}{root}', headers=headers, data=data)

            if r.status_code == 200:
                r = r.json()
                return r
            elif r.status_code == 401:
                self.get_token()
            elif r.status_code == 429:
                retry_request += 1
                if retry_request < 4:
                    time.sleep(1)
                else:
                    retry_request = 0
                    date_now = datetime.now()
                    time_to_min = 3600 - (date_now.minute) * 60
                    time_to_sleep = time_to_min + 120
                    logger.debug(f"Limit request script sleeping at {date_now}, {time_to_sleep / 60} min")
                    time.sleep(time_to_sleep)
            else:
                logger.error(f'Could not resolve {self.site}{root}, returned error {r.status_code}')
                break
        return None
