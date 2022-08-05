from fastapi import status, HTTPException, Depends
from fastapi import APIRouter
from keycloak import KeycloakOpenID

from app.settings import get_settings
from app.schemas.user_schema import User
from app.libs.keycloak.admin_func import KeycloakAdminConfig
from keycloak.exceptions import KeycloakPostError


settings = get_settings()

test_route = APIRouter(tags=['test'])

@test_route.get(path='/loging')
async def login(login: str, password: str):
    keycloak_openid = KeycloakOpenID(server_url=f'{settings.KEYCLOAK_SERVER_ADDRESS}auth/',
                                     client_id=settings.KEYCLOAK_CLIENT,
                                     realm_name=settings.KEYCLOAK_REALM_NAME,
                                     client_secret_key=settings.KEYCLOAK_CLIENT_SECRET_KEY)
    try:
        token = keycloak_openid.token(login, password)
    except KeycloakPostError:
        raise HTTPException(404, 'User not found')
    return token['access_token']


async def auth_required(token):
    keycloak_openid = KeycloakOpenID(server_url=f'{settings.KEYCLOAK_SERVER_ADDRESS}auth/',
                                     client_id=settings.KEYCLOAK_CLIENT,
                                     realm_name=settings.KEYCLOAK_REALM_NAME,
                                     client_secret_key=settings.KEYCLOAK_CLIENT_SECRET_KEY)

    KEYCLOAK_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\n" + keycloak_openid.public_key() + "\n-----END PUBLIC KEY-----"
    options = {"verify_signature": True, "verify_aud": True, "verify_exp": True}
    token_info = keycloak_openid.decode_token(token, key=KEYCLOAK_PUBLIC_KEY, options=options)
    return token_info

@test_route.get(path='/test',)
async def get_test_private_data(token = Depends(auth_required)):

    return token['sub']
