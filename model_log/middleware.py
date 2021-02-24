try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

from . import _local


class ModelLogMiddleware(MiddlewareMixin):
    """Expose request to the local variable.
        This middleware sets request as a local thread variable, making it
        available to the methods to allow tracking of the authenticated user
        making a change.
    """

    def process_request(self, request):
        _local.request = request

    def process_response(self, request, response):
        if hasattr(_local, "request"):
            del _local.request
        return response
