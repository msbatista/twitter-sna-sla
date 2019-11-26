from repository.mongo_repository import MongoRepository
from settings import TwitterAuths
from stream_handler.base.base_stream import BaseStream
from stream_handler.stream_handler import StreamHandler


class StreamBusiness:
    def __init__(self, time_out: int = 180):
        self.mongo_repository = MongoRepository()
        self.stream = BaseStream(TwitterAuths.CONSUMER_KEY,
                                 TwitterAuths.CONSUMER_SECRET,
                                 TwitterAuths.ACCESS_TOKEN,
                                 TwitterAuths.ACCESS_TOKEN_SECRET,
                                 listener=StreamHandler(),
                                 time_out=time_out
                                 )

    def stream_tweets(self, track: list = None):
        document = self.stream.filter(track=track)
        self._save_to_mongo(document=document)

    def _save_to_mongo(self, document: dict):
        self.mongo_repository.insert_one(document=document)
