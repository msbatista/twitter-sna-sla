from tweepy import OAuthHandler, StreamListener, Stream

from meta.singleton import Singleton


class BaseStream(metaclass=Singleton, Stream):
    def __init__(self,
                 consumer_key: str,
                 consumer_secret: str,
                 access_token: str,
                 access_token_secret: str,
                 listener: StreamListener = None,
                 time_out: int = 24 * 60 * 60 * 7):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        super().__init__(auth=auth, listener=listener, timeout=time_out)
