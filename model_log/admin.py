from django.contrib import admin

from model_log.mixins import ModelAdminMixin
from .models import Log


class LogAdmin(admin.ModelAdmin):
    fields = ('object_id', 'model', 'action', 'data', 'date_created', 'user')

    list_display = ('id', 'object_id', 'model', 'action', 'date_created')

    readonly_fields = ('object_id', 'model', 'action', 'data', 'date_created', 'user')

    search_fields = ('id', 'object_id', 'model', 'action', 'date_created', 'user')

    change_form_template = "change_form.html"

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class LogModelAdmin(ModelAdminMixin, admin.ModelAdmin):
    """ Use this class instead of ModelAdmin. """
    pass


admin.site.register(Log, LogAdmin)
