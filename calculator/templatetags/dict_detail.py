from django import template
register = template.Library()


@register.filter
def dict_detail(dict, key):
    return dict[key][0]