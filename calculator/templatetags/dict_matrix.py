from django import template
register = template.Library()


@register.filter
def dict_matrix(dict, key):
    return dict[key][1]