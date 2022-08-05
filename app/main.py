from fastapi import FastAPI
from uvicorn import run

from app.routes.test_route import test_route
from app.routes.user_registration_route import user_registration_router


app = FastAPI(
    title="Keycloak",
    description="**[Documentation]**",
)
app.router.include_router(user_registration_router)
app.router.include_router(test_route)

@app.get('/')
def index():
    return {'test_route': 'test message'}


def main() -> None:
    run(
        app,
        host='0.0.0.0',
        port=8080
    )