from django.apps import AppConfig


class ModelLogConfig(AppConfig):
    name = 'model_log'

    def ready(self):
        from .setup import register_signals
        register_signals()
