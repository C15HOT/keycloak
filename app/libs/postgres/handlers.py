from fastapi import HTTPException, status
from sqlalchemy import insert, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from app.libs.postgres.models import Users
from app.schemas.user_schema import UsersSchema
from app.settings import get_settings

settings = get_settings()




def insert_user(user: UsersSchema):
    connection = settings.AVATAR_DB
    engine = create_engine(connection)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_user = Users(id=user.id,
                     username=user.username,
                     firstname=user.firstname,
                     lastname=user.lastname,
                     middlename=user.middlename,
                     gender=user.gender,
                     birthday=user.birthday,
                     photo_uri=user.photo_uri,
                     is_online=user.is_online
                     )
    if session.query(exists().where(Users.username == new_user.username)).scalar() == True:
        return HTTPException(status.HTTP_409_CONFLICT, detail='A user with this name exists')

    else:
        session.add(new_user)
        session.commit()

