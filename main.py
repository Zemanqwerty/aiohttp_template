from aiohttp import web
from app.settings import config
from aiohttp_session import session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from os import urandom
from aiohttp_auth import auth
import asyncio
from typing import List
import aiohttp_jinja2
import jinja2


def setup_config(application):
    application['config'] = config


def setup_routes(application):
    from app.test_app.routes import setup_routes as setup_app_routes
    setup_app_routes(application)


def setup_external_libraries(application: web.Application) -> None:
    aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader("templates"))


def setup_app(application):
    setup_external_libraries(application)
    setup_routes(application)


policy = auth.SessionTktAuthentication(urandom(32), 60, include_ip=True)

middlewares = [session_middleware(EncryptedCookieStorage(urandom(32))),
                auth.auth_middleware(policy)]

app = web.Application(middlewares=middlewares)


if __name__ == "__main__":
    setup_app(app)
    web.run_app(app, host='localhost', port=config['common']['port'])
