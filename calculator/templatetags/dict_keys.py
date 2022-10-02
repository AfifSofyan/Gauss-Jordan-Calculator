from django import template
register = template.Library()


@register.filter
def dict_keys(dict):
    return dict.keys()
