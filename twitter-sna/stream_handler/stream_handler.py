import json

from interface.stream_handler.i_stream_handler import IStreamHandler


class StreamHandler(IStreamHandler):
    def on_data(self, raw_data):
        return json.loads(raw_data)
