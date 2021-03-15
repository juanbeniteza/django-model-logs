from django.contrib.contenttypes.models import ContentType
from .models import Log
from . import _local


def model_to_dict(instance):
    opts = instance._meta

    ignore_fields = getattr(instance, 'LOGGING_IGNORE_FIELDS', [])
    only_fields = getattr(instance, 'LOGGING_ONLY_FIELDS', [])

    if only_fields:
        field_names = [f.attname for f in opts.fields if f.name in only_fields]
    elif ignore_fields:
        field_names = [f.attname for f in opts.fields if f.name not in ignore_fields]
    else:
        field_names = [f.attname for f in opts.fields]

    data = {f: getattr(instance, f, None) for f in field_names}

    return data


def diff(obj):
    d1 = obj.__attrs
    d2 = model_to_dict(obj)
    diffs = [(k, d2[k]) for k, v in d1.items() if v != d2[k]]
    return dict(diffs)


def create_log(obj, action, db, data=None):

    user = _local.request.user.id if _local.request else "System User"

    if data or action == 'C':
        log_data = {
            'object_id': obj.pk,
            'model': ContentType.objects.get_for_model(obj._meta.model).model,
            'action': action,
            'data': data,
            'user': user
        }

        Log.objects.using(db).create(**log_data)

