from django.conf import settings
from django.forms.utils import flatatt
from django.template.loader import render_to_string
from django.utils.html import mark_safe
from django.utils.module_loading import import_string

config = {
    # all renderers available to the user
    "renderers": {
        "sprites": "easy_icons.renderers.sprites",
        "provider": "easy_icons.renderers.provider",
        "svg": "easy_icons.renderers.svg",
    },
    # the function that will be used to get the icon based on user settings
    "default_renderer": "provider",
    # default attributes applied to all icons
    "attrs": {},
    # directory where SVG icons are stored
    "svg_dir": "icons",
    # default tag for class-based icons
    "tag": "i",
    # maps aliases to icon names
    "aliases": {},
    # maps named icons to classes (for use with libraries like Font Awesome)
    "classmap": {},
    # URL for the external sprite file (if used)
    "sprite_url": None,
}

config.update(getattr(settings, "EASY_ICONS", {}))


def _attrs(**kwargs):
    """Merges the defaults with the user-provided attributes."""

    if not kwargs.get("defaults"):
        return flatatt(kwargs)
    defaults = config.get("attrs").copy()
    defaults.update(kwargs)
    return flatatt(defaults)


def _svg_handler(svg_str, **kwargs):
    """Injects attrs into the svg element and returns a marksafe svg icon."""
    first, sep, rest = svg_str.partition("<svg")
    return mark_safe(f"{first}{sep}{_attrs(**kwargs)} {rest}")  # noqa: S308


def sprites(name, **kwargs):
    """Renders SVG icons using an external sprites file."""
    svg_str = f'<svg><use xlink:href="{config.get("sprite_url")}#{name}" /></svg>'
    return _svg_handler(svg_str, **kwargs)


def provider(name, **kwargs):
    # icon_class = config.get("classmap").get(name, name)
    if name.endswith(".svg"):
        # when provider is the default renderer, the user may override it by passing an alias with the .svg extension
        return svg(name.replace(".svg", ""), **kwargs)

    tag = kwargs.pop("tag", config.get("tag"))
    extra_class = kwargs.pop("class", "")
    # defaults = kwargs.pop("defaults")
    template = f"<{tag} class='{name} {extra_class}'{_attrs(**kwargs)}></{tag}>"
    return mark_safe(template)  # noqa: S308


def svg(name, **kwargs):
    """Uses Django's template loader to embed an SVG directly in the HTML file."""
    svg_str = render_to_string(f"{config.get('svg_dir')}/{name}.svg")
    return _svg_handler(svg_str, **kwargs)


def icon(name, **kwargs):
    # get the correct name, accounting for any aliases
    name = config["aliases"].get(name, name)

    # the renderer to use can be passed as a keyword argument
    renderer = kwargs.pop("renderer", config.get("default_renderer"))

    # the function that will be used to get the icon based on user settings
    renderer = import_string(config["renderers"].get(renderer))
    return renderer(name, **kwargs)
