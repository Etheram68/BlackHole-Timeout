import os, io
import pandas as pd
from datetime import datetime
from fastapi import FastAPI, status
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
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

app.add_middleware(CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/blackhole-timeout", response_model=models.UsersBlackholeResponse, status_code=status.HTTP_200_OK, tags=['Users'], openapi_extra={"requestBody": None})
def users_blackhole_timeout(page:int = 1, nb_per_page:int = 20, blackhole:int = 30):
    results = user_manager.get_users_blackhole(page_number=page - 1, page_size=nb_per_page, blackhole=blackhole)
    return models.UsersBlackholeResponse(
        success=True,
        timestamp=datetime.utcnow(),
        status='OK',
        message='Done',
        data=results,
    )


@app.get("/users/blackhole-timeout/csv", response_class=StreamingResponse, status_code=status.HTTP_201_CREATED, tags=['Users'], openapi_extra={"requestBody": None})
def users_blackhole_export(blackhole:int = 30):
    results = user_manager.get_users_blackhole_csv(blackhole)
    logger.debug([obj.dict() for obj in results])
    df = pd.DataFrame([obj.dict() for obj in results])
    stream = io.StringIO()
    df.to_csv(stream)
    return StreamingResponse(
        iter([stream.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=UsersBlackhole.csv",
            'Access-Control-Expose-Headers': 'Content-Disposition'
        }
    )
