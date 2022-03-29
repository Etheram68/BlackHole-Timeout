import os

from datetime import datetime
from fastapi import FastAPI, status
from src.logger.logger import logger as logger_main
from src.entity_models import models
from src.dao.dao_factory import DaoFactory

app = FastAPI(root_path=os.environ.get('ROOT_PATH', ''))

logger = logger_main.getChild(__name__)
dao_factory = DaoFactory()
dao_user = dao_factory.get_dao_user()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/blackhole-timeout", response_model=models.UsersBlackholeResponse, status_code=status.HTTP_200_OK, tags=['Users'], openapi_extra={"requestBody": None})
def users_blackhole_timeout():
    results = dao_user.get_users_blackhole()
    logger.debug(results)
    return models.UsersBlackholeResponse(
        success=True,
        timestamp=datetime.utcnow(),
        status='OK',
        message='Done',
        data=results
    )

