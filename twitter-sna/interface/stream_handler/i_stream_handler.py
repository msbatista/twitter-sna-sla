from tweepy import StreamListener


class IStreamHandler(StreamListener):

    def on_data(self, raw_data):
        raise NotImplementedError

    def on_connect(self):
        print("Connecting...")

    def on_error(self, status_code):
        print("An error occurred: {status_code}".format(status_code=status_code))
        return False

    def on_timeout(self):
        print("Timeout reached.")
        return

    def on_exception(self, exception):
        print("Exception occurred: " + str(exception))
