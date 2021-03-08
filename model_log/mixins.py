from django.contrib.admin.utils import unquote
from django.core.exceptions import PermissionDenied
from django.template.response import TemplateResponse
from django.utils.text import capfirst
from django.utils.translation import gettext as _
from model_log.models import Log


class ModelAdminMixin:
    object_history_template = "object_history.html"

    def history_view(self, request, object_id, extra_context=None):
        "The 'history' admin view for this model."
        from django.contrib.admin.models import LogEntry
        # First check if the user can see this history.
        model = self.model
        obj = self.get_object(request, unquote(object_id))
        if obj is None:
            return self._get_obj_does_not_exist_redirect(request, model._meta, object_id)

        if not self.has_view_or_change_permission(request, obj):
            raise PermissionDenied

        # Then get the history for this object.
        opts = model._meta
        app_label = opts.app_label
        log_data = Log.objects.filter(
            model=obj.__class__.__name__.lower(),
            object_id=object_id)

        context = {
            **self.admin_site.each_context(request),
            'title': _('Change history: %s') % obj,
            'action_list': log_data,
            'module_name': str(capfirst(opts.verbose_name_plural)),
            'object': obj,
            'opts': opts,
            'preserved_filters': self.get_preserved_filters(request),
            **(extra_context or {}),
        }

        request.current_app = self.admin_site.name

        return TemplateResponse(request, self.object_history_template or [
            "admin/%s/%s/object_history.html" % (app_label, opts.model_name),
            "admin/%s/object_history.html" % app_label,
            "admin/object_history.html"
        ], context)
