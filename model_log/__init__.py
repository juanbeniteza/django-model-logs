from threading import local

default_app_config = 'model_log.apps.ModelLogConfig'


class _Local(local):
    """
    Class for storing the request as local variable per thread
    """
    def __init__(self):
        self.request = None


_local = _Local()
