from pydantic import BaseModel
from pydantic.types import UUID4
from datetime import datetime, date
from typing import Optional
from enum import Enum

class Gender(Enum):
    male = 'male'
    female = 'female'
    other = 'other'

class UsersSchema(BaseModel):
    id: Optional[UUID4]
    username: str
    firstname: str
    lastname: str
    middlename: str
    gender: str
    birthday: date
    photo_uri: str
    # join_data: date
    is_online: bool
    # last_seen: datetime

    email: str
    password: str

