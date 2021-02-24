from django.conf import settings

MODELS_FOR_LOGGING = getattr(settings, 'MODELS_FOR_LOGGING', [])
MODELS_FOR_EXCLUDE = getattr(settings, 'MODELS_FOR_EXCLUDE', [])