class TelnetClient:

    def __init__(self):
        print 'init'

    def __enter__(self):
        print 'enter has been called'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'exit has been called'

    @staticmethod
    def start():
        print 'start has been called'


with TelnetClient() as client:
    client.start()
