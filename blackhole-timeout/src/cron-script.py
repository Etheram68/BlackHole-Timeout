import time, os
import src.entity_models.models as models

from bson.objectid import ObjectId
from src.api.School42Client import School42Client
from src.logger.logger import logger as logger_main
from datetime import datetime
from src.dao.dao_factory import DaoFactory
from src.core.DateManager import DateManager
from src.core.UserManager import UserManager


logger = logger_main.getChild(__name__)
dao_factory = DaoFactory()
user_manager = UserManager(dao_factory)
date_manager = DateManager(dao_factory)

def get_campus_id(campus_name):
    payload = {'filter[name]': campus_name}
    r = scholl_42.get(root='/v2/campus', data=payload)[0]

    logger.debug(r)
    if r and len(r) and r['active']:
        return r['id']
    logger.error(f'Campus not exist or not active Json: {r}')
    exit()


def get_users_info(users):
    for user in users:
        time.sleep(0.2)
        r = scholl_42.get(f'/v2/users/{user}')

        if not r:
            logger.error(f'Error with user_id {user}')
            continue
        if r['staff?'] or r['alumni'] or r['is_launched?']:
            continue

        lst_cursus = r['cursus_users']
        find_cursus = [c['blackholed_at'] for c in lst_cursus if c['cursus_id'] == 21]
        if not find_cursus:
            continue
        black_hole = find_cursus[0]
        if not black_hole:
            continue
        projects_users = [p['project'] for p in r['projects_users'] \
                if p['project']['id'] == models.Project.EXAM_06 or \
                   p['project']['id'] == models.Project.FT_TRANSCENDENCE]
        logger.info(f'User has validate {len(projects_users)} project for end common core')
        if len(projects_users):
            continue
        black_hole_obj = datetime.strptime(black_hole[:-1], "%Y-%m-%dT%H:%M:%S.%f")
        day_left = black_hole_obj - date_now
        if day_left.days < 0:
            continue

        users = models.User(
            id=ObjectId(),
            user_id=r['id'],
            login=r['login'],
            url=r['url'],
            image_url=r['image_url'],
            black_hole_at=str(day_left),
            days_left=day_left.days
        )
        logger.info(users)
        user_manager.add_user(users)
    return users


def get_id_users_campus(id_campus):
    i = 0
    users_id = []

    while (True):
        payload = {'filter[campus_id]': id_campus, 'sort': '-created_at', 'page[size]': '100', 'page[number]': i}
        r = scholl_42.get(root='/v2/campus_users', data=payload)
        if not r:
            break ;
        users_id.extend([o['user_id'] for o in r])
        time.sleep(0.5)
        i += 1
    return users_id


if __name__ == '__main__':
    date_now = datetime.now()
    try:
        scholl_name = os.environ.get('SCHOOL_NAME')
        scholl_42 = School42Client(
            client_id=os.environ['API_KEY_UID'],
            client_secret=os.environ['API_KEY_SECRET']
        )
    except KeyError:
        logger.error('API_KEY_UID or API_KEY_SECRET not found')
        exit()
    result = date_manager.get_date()
    code = scholl_42.get_token()
    logger.debug(code)
    id_campus = get_campus_id(scholl_name)
    logger.debug(result)
    if not result:
        date_manager.update_date()
        users_id = get_id_users_campus(id_campus)
    else:
        users_id = user_manager.get_users()
    users = get_users_info(users_id)
