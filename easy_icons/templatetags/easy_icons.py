from django import template
from django.conf import settings
from django.forms.utils import flatatt
from django.template.loader import render_to_string
from django.utils.html import mark_safe

register = template.Library()


@register.simple_tag
def icon(icon: str, nodefaults=False, **kwargs):
    """Retrieves the default icon for a given object."""

    ICONS_DIR = getattr(settings, "easy_icons_ICONS_DIR", "icons")
    # allow user to pass in the icon with or without the extension
    icon = icon.split(".")[0]
    if nodefaults:
        return mark_safe(render_to_string(f"{ICONS_DIR}/{icon}.svg"))

    DEFAULTS = getattr(
        settings,
        "easy_icons_DEFAULTS",
        {
            "height": "1em",
            "fill": "currentColor",
        },
    )
    DEFAULTS.update(kwargs)

    svg_str = render_to_string(f"{ICONS_DIR}/{icon}.svg")
    first, sep, rest = svg_str.replace("\n", "").partition("><")

    return mark_safe(f"{first}{flatatt(DEFAULTS)}{sep}{rest}")  # noqa: S308
