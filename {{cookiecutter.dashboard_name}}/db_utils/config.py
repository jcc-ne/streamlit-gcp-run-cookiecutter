from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))

load_dotenv(path.join(basedir, ".env"))

# Database config
DATABASE_HOST = environ.get("DATABASE_HOST")
DATABASE_HOST_EVENTS = environ.get("DATABASE_HOST_EVENTS")
DATABASE_USER = environ.get("DATABASE_USER")
DATABASE_PASSWORD = environ.get("DATABASE_PASSWORD")
DATABASE_PORT = environ.get("DATABASE_PORT")
DATABASE_NAME = environ.get("DATABASE_NAME")
DATABASE_EVENTS_PORT = environ.get("DATABASE_EVENTS_PORT")

REDIS_HOST = environ.get("REDIS_HOST")
REDIS_PORT = environ.get("REDIS_PORT")

LOG_LEVEL = environ.get("LOG_LEVEL", 10)
APP_ENV = environ.get("APP_ENV", "DEV")
