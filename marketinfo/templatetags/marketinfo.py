from django import template

register = template.Library()

@register.filter
def get_field_value(instance, field_name):
    """
    Custom template filter to get the value of a field for a given instance.
    """
    return getattr(instance, field_name, "")
