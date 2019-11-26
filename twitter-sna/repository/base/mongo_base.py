from pymongo import MongoClient

from meta.singleton import Singleton
from settings import MongoSettings


class BaseRepository(metaclass=Singleton):
    def __init__(self):
        _client = MongoClient(MongoSettings.MONGO_URI)
        db = _client[MongoSettings.MONGO_DB]
        self.collection = db[MongoSettings.MONGO_COLLECTION]
