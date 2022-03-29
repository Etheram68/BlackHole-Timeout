import os

from fastapi import FastAPI

app = FastAPI(root_path=os.environ.get('ROOT_PATH', ''))


@app.get("/")
def read_root():
    return {"Hello": "World"}
