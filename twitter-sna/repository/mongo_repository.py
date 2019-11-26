from .base.mongo_base import BaseRepository


class MongoRepository(BaseRepository):
    def insert_one(self, document: dict):
        self.collection.insert_one(document=document)