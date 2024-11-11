from django import template

from easy_icons import renderers

register = template.Library()


@register.simple_tag
def icon(icon: str, defaults=True, **kwargs):
    """Retrieves the default icon for a given object."""
    return renderers.icon(icon, defaults=defaults, **kwargs)
