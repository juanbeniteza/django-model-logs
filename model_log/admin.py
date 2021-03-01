from django.contrib import admin
from .models import Log


class LogAdmin(admin.ModelAdmin):
    fields = ('object_id', 'model', 'action', 'data', 'date_created', 'user')

    list_display = ('id', 'object_id', 'model', 'action', 'date_created')

    readonly_fields = ('object_id', 'model', 'action', 'data', 'date_created', 'user')

    search_fields = ('id', 'object_id', 'model', 'action', 'date_created', 'user')


admin.site.register(Log, LogAdmin)