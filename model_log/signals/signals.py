from ..utils import model_to_dict, diff, create_log


def save_object(sender, instance, created, using, **kwargs):
    data = diff(instance)
    action = 'C' if created else 'U'
    create_log(instance, action, using, data)


def init_object_attrs(sender, instance, **kwargs):
    model_dict = {}

    if instance.id:
        model_dict = model_to_dict(instance)
    instance.__attrs = model_dict


def delete_object(sender, instance, using, **kwargs):
    data = {}
    action = 'D'
    create_log(instance, action, using, data)
