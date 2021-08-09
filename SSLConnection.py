import os, ssl


class SSLConnection:
    def __init__(self):
        pass

    def ssl_connection(self):
        if not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
            ssl._create_default_https_context = ssl._create_unverified_context
        return ssl._create_default_https_context
