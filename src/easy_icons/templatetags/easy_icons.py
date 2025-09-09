"""Template tags for django-easy-icons.

This module provides Django template tags for rendering icons in templates.
The main template tag is {% icon %} which integrates with the django-easy-icons
rendering system.

Usage in templates:
    {% load easy_icons %}

    <!-- Basic usage -->
    {% icon "home" %}

    <!-- With attributes -->
    {% icon "user" class="nav-icon" height="2em" %}

    <!-- Using specific renderer -->
    {% icon "heart" renderer="fontawesome" %}

    <!-- With template variables -->
    {% icon icon_name class=css_class %}

The template tag supports all the same functionality as the Python icon() function,
including multiple renderers, attribute merging, and Django's automatic HTML escaping.
"""

from django import template
from django.utils.safestring import SafeString

from .. import utils

register = template.Library()


@register.simple_tag
def icon(name: str, renderer: str = "default", **kwargs) -> SafeString:
    """Template tag to render an icon.

    Usage:
        {% icon "home" %}
        {% icon "home" renderer="fontawesome" %}
        {% icon "home" renderer="sprites" %}
        {% icon "home" class="large" height="2em" %}
        {% icon "heart" renderer="fontawesome" class="gold" %}

    Args:
        name: The icon name to render
        renderer: Name of the renderer to use (defaults to 'default')
        **kwargs: Additional attributes for the icon

    Returns:
        Safe HTML string containing the rendered icon
    """
    return utils.icon(name, renderer=renderer, **kwargs)
