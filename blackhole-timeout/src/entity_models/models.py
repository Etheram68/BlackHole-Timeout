from enum import Enum
from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from datetime import datetime

class ObjectIdPyd(str):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            if ObjectId.is_valid(v):
                return ObjectId(v)
            else:
                raise TypeError(f"Not a valid ObjectId string: {v}")
        return v

class Base(BaseModel):
    id: ObjectIdPyd = Field(None, alias='_id')

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: lambda x: str(x),
            ObjectIdPyd: lambda x: x.valueOf(),
            datetime: lambda dt: dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        }


class User(BaseModel):
    user_id: str
    login: str
    url: str
    image_url: str
    black_hole_at: str
    days_left: int

class Project(int, Enum):
    EXAM_06 = 1324
    FT_TRANSCENDENCE = 1337
