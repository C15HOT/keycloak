from fastapi import status, HTTPException
from fastapi import APIRouter
from app.settings import get_settings
from app.schemas.user_schema import UsersSchema
from app.libs.keycloak.admin_func import KeycloakAdminConfig
from keycloak.exceptions import KeycloakPostError
from app.libs.postgres.handlers import insert_user

settings = get_settings()

user_registration_router = APIRouter(tags=['registration'])

@user_registration_router.post(path='/registration',
                          summary='user registration')
async def registration(user: UsersSchema):
    keycloak = KeycloakAdminConfig()

    try:
        keycloak.create_user(username=user.username,
                             email=user.email,
                             first_name=user.firstname,
                             last_name=user.lastname,
                             password=user.password
                             )
        user_id_keycloak = keycloak.keycloak_admin.get_user_id(user.username)
        user.id = user_id_keycloak

    except KeycloakPostError:
        raise HTTPException(409, "User exists with same username or email")
    try:
        insert_user(user)
    except Exception:
        keycloak.keycloak_admin.delete_user(user_id=user.id)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Не удалось записать юзера в БД')
    return status.HTTP_201_CREATED