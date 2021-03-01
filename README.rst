===========
Model Logs
===========

Model logs is a Django app for storing changes of yours objects

Quick start
-----------

1. Add "model_log" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'model_log',
    ]


2. Run ``python manage.py migrate`` to create the "model_logs" models.

3. For adding or excluding the models you want to log, in the ``settings.py``::

    MODELS_FOR_LOGGING = (
        'app.ClassName',    # logging only for this model
        'another_app'     # logging of all models in this app
    )

    MODELS_FOR_EXCLUDE = (
        'app.ClassName',    # excluding from logging only for this model
    )

