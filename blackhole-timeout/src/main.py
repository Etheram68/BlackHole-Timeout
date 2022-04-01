import os
from datetime import datetime
from fastapi import FastAPI, status
from src.logger.logger import logger as logger_main
from src.entity_models import models
from src.dao.dao_factory import DaoFactory
from src.core.DateManager import DateManager
from src.core.UserManager import UserManager

app = FastAPI(root_path=os.environ.get('ROOT_PATH', ''))

logger = logger_main.getChild(__name__)
dao_factory = DaoFactory()
user_manager = UserManager(dao_factory)
date_manager = DateManager(dao_factory)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/blackhole-timeout", response_model=models.UsersBlackholeResponse, status_code=status.HTTP_200_OK, tags=['Users'], openapi_extra={"requestBody": None})
def users_blackhole_timeout(page:int = 1):
    results = user_manager.get_users_blackhole(page - 1)
    return models.UsersBlackholeResponse(
        success=True,
        timestamp=datetime.utcnow(),
        status='OK',
        message='Done',
        data=results
    )
