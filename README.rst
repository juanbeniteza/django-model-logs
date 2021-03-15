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

2. Add "ModelLogMiddleware" to your MIDDLEWARE setting like this::

    MIDDLEWARE = [
        ...
        'model_log.middleware.ModelLogMiddleware',
    ]


3. Run ``python manage.py migrate`` to create the "model_logs" models.

4. For adding or excluding the models you want to log, in the ``settings.py``::

    MODELS_FOR_LOGGING = (
        'app.ClassName',    # logging only for this model
        'another_app'     # logging of all models in this app
    )

    MODELS_FOR_EXCLUDE = (
        'app.ClassName',    # excluding from logging only for this model
    )

5. To override Django's default view to show the history of a log, use LogModelAdmin instead of ModelAdmin::

    class ExampleAdmin(LogModelAdmin):
        pass