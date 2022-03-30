import pathlib
import yaml
import asyncio


DEBUG = True

# указываем директорию проекта
BASE_DIR = pathlib.Path(__file__).parent.parent

# указываем путь к конфигурационному файлу
config_path = BASE_DIR / 'config' / 'config.yaml'


# обрабатываем конфигурационный файл
def get_config(path):
    with open(path) as f:
        parsed_config = yaml.safe_load(f)
        return parsed_config


config = get_config(config_path)


# В зависимости от переменной DEBUG переключаем окружение ОС
# True - Windows / False - unix
def debug_settings():
    if DEBUG == True:
        asyncio.set_event_loop_policy(
            asyncio.WindowsSelectorEventLoopPolicy()
        )



# данные для подключения к постгрес
if DEBUG == True:
    DB_HOST = 'localhost'
    DB_PASSWORD = 'Gast3864'
    DB_PORT = 5432
    DB_USER = 'postgres'
    DB_NAME = 'app'
else:
    DB_HOST = 'pg_db'
    DB_PASSWORD = 'root'
    DB_PORT = 5432
    DB_USER = 'postgres'
    DB_NAME = 'app'
