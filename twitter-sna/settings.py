import os

from decouple import config

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TwitterAuths:
    CONSUMER_KEY = config("CONSUMER_KEY")
    CONSUMER_SECRET = config("CONSUMER_SECRET")
    ACCESS_TOKEN = config("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = config("ACCESS_TOKEN_SECRET")


class MongoSettings:
    MONGO_URI = config("MONGO_URI")
    MONGO_DB = config("MONGO_DB")
    MONGO_COLLECTION = config("MONGO_COLLECTION")