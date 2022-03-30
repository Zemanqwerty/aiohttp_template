from multiprocessing.spawn import prepare
from pydoc import cli
from socket import socket
from tkinter.tix import Tree
from aiohttp import web
import json
import aiohttp
from loguru import logger
from app.settings import BASE_DIR
import psycopg
import hashlib
from .. import settings
import asyncio
from aiohttp_auth import auth
from datetime import datetime as dt
from aiohttp import ClientSession
from typing import List, Union
import aiohttp_jinja2

from ..settings import debug_settings as setup_debug


setup_debug()


# формируем файл логов
logger.add(f'{BASE_DIR}/logs/info.json', format='{time} {level} {message}',
           level='INFO', rotation='100 KB', compression='zip', serialize=True)


# декоратор для аутентификации пользователя
def api_authentication_check(function):
    async def wrapped(request: web.Request) -> web.Response:
        # получаем данные пользователя
        user = await auth.get_auth(request)
        # если пользователь не авторизован
        if user is None:
            # формируем json
            response_obj = {
                'status': 'failed',
                'message': 'user is not authenticated'
            }
            return web.Response(text=json.dumps(response_obj), status=400)
        # если пользователь авторизован
        else:
            return await function(request)
    return wrapped


@logger.catch()
@api_authentication_check
async def api_logout(request):
    try:
        # выводим пользователя из сети
        await auth.forget(request)
        # формируем json
        response_obj = {
            'status': 'success',
            'message': 'user has logged out'
        }
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        # формируем json
        response_obj = {
            'status': 'failed',
            'message': str(e)
        }
        return web.Response(text=json.dumps(response_obj), status=500)


# функция регистрации пользователя
@logger.catch()
async def api_registration(requset: web.Request) -> web.Response:
    try:
        # получаем json и сохраняем в переменную
        json_data = await requset.json()

        # обращаемся к словарю по ключу
        username = json_data['username']
        password = json_data['password']

        try:
            # соединение с БД
            async with await psycopg.AsyncConnection().connect(dbname=settings.DB_NAME, user=settings.USER, password=settings.PASSWORD, port=settings.PORT, host=settings.HOST) as conn:
                async with conn.cursor() as cur:
                    pass
                cur.close()
            # сохраняем изменения и закрываем подключение к БД
            conn.commit()
            conn.close()
        # исключение при подключении к БД
        except Exception() as error:
            pass
    # исключение при работе с json
    except Exception() as error:
        pass
    finally:
        pass


# функция регистрации пользователя
@logger.catch()
async def api_registration(requset: web.Request) -> web.Response:
    try:
        # получаем json и сохраняем в переменную
        json_data = await requset.json()

        # обращаемся к словарю по ключу
        username = json_data['username']
        password = json_data['password']

        try:
            # соединение с БД
            async with await psycopg.AsyncConnection().connect(dbname=settings.DB_NAME, user=settings.USER, password=settings.PASSWORD, port=settings.PORT, host=settings.HOST) as conn:
                async with conn.cursor() as cur:
                    pass
                cur.close()
            # сохраняем изменения и закрываем подключение к БД
            conn.commit()
            conn.close()
        # исключение при подключении к БД
        except Exception() as error:
            pass
    # исключение при работе с json
    except Exception() as error:
        pass
    finally:
        pass


@aiohttp_jinja2.template('client/test_page.html')
async def test_page(requset):
    return {'txt': 'some text'}