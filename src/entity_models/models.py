from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    login: str
    url: str
    image_url: str
    black_hole_at: str
