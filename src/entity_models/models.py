from enum import Enum
from pydantic import BaseModel


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
