from app.settings import get_settings
from keycloak import KeycloakAdmin
settings = get_settings()

class KeycloakAdminConfig:
    def __init__(self):
        self.keycloak_admin = KeycloakAdmin(
            server_url=f'{settings.KEYCLOAK_SERVER_ADDRESS}auth/',
            username=settings.KEYCLOAK_USER,
            password=settings.KEYCLOAK_PASSWORD,
            realm_name=settings.KEYCLOAK_REALM_NAME,
            user_realm_name=settings.KEYCLOAK_REALM_NAME,
            client_id=settings.KEYCLOAK_CLIENT,
            client_secret_key=settings.KEYCLOAK_CLIENT_SECRET_KEY,
            verify=True
        )

    def create_user(self, email, username, first_name, last_name, password):
        self.keycloak_admin.create_user(
            {"email": email,
            "username": username,
            "enabled": True,
            "firstName": first_name,
            "lastName": last_name,
            "credentials": [{"value": password,"type": "password",}]},
            exist_ok=False
        )