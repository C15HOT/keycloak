from fastapi import status, HTTPException
from fastapi import APIRouter
from app.settings import get_settings
from app.schemas.user_schema import User
from app.libs.keycloak.admin_func import KeycloakAdminConfig
from keycloak.exceptions import KeycloakPostError


settings = get_settings()

user_registration_router = APIRouter(tags=['registration'])

@user_registration_router.post(path='/registration',
                          summary='user registration')
async def registration(user: User):
    keycloak = KeycloakAdminConfig()
    try:
        keycloak.create_user(**user.dict())
    except KeycloakPostError:
        raise HTTPException(409, "User existts with same username")
    return status.HTTP_201_CREATED