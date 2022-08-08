from sqlalchemy import  Boolean, Column, Date, DateTime, Enum,String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Users(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    middlename = Column(String)
    gender = Column(Enum('male', 'female', 'other', name='GENDER_TYPE'), nullable=False)
    birthday = Column(Date, nullable=False)
    photo_uri = Column(String, nullable=False)
    join_date = Column(Date, nullable=False, server_default=text("now()"))
    is_online = Column(Boolean, nullable=False, server_default=text("false"))
    last_seen = Column(DateTime, nullable=False, server_default=text("now()"))