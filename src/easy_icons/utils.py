"""Main interface functions for django-easy-icons.

This module provides the primary public API for the django-easy-icons package,
including renderer management, caching, and the main icon() function used by
both Python code and template tags.

Functions:
    get_renderer(name): Get a configured renderer instance by name
    clear_cache(): Clear the renderer instance cache
    icon(name, renderer, **kwargs): Render an icon using the specified renderer

The icon() function is the main entry point for rendering icons and supports:
- Multiple configured renderers
- Attribute merging and customization
- Caching for performance
- Integration with Django's SafeString for secure HTML output

Example:
    # Basic usage
    home_icon = icon("home")

    # With custom attributes
    user_icon = icon("user", **{"class": "large", "data-role": "button"})

    # Using named renderer
    fa_icon = icon("heart", renderer="fontawesome")
"""

from typing import Any, cast

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import import_string
from django.utils.safestring import SafeString

# Simple module-level cache for renderer instances
_renderer_cache: dict[str, Any] = {}


def get_renderer(name: str = "default") -> Any:
    """Get a configured renderer instance.

    Args:
        name: Name of the renderer to get (defaults to 'default')

    Returns:
        Configured renderer instance

    Raises:
        ImproperlyConfigured: If renderer is not configured or cannot be imported
    """
    # Check cache first
    if name in _renderer_cache:
        return _renderer_cache[name]

    # Get configuration from settings or use empty dict
    config = getattr(settings, "EASY_ICONS", {})

    # Validate basic configuration structure
    if not isinstance(config, dict):
        raise ImproperlyConfigured("EASY_ICONS setting must be a dictionary")

    # Ensure requested renderer exists
    if name not in config:
        raise ImproperlyConfigured(f"Renderer '{name}' is not configured in EASY_ICONS")

    renderer_config = config[name]

    # Validate renderer configuration structure
    if not isinstance(renderer_config, dict):
        raise ImproperlyConfigured(f"EASY_ICONS['{name}'] must be a dictionary")

    if "renderer" not in renderer_config:
        raise ImproperlyConfigured(f"EASY_ICONS['{name}'] must specify a 'renderer' class path")

    # Import and instantiate the renderer class
    renderer_class_path = renderer_config["renderer"]

    try:
        renderer_class = import_string(renderer_class_path)
    except ImportError as e:
        raise ImproperlyConfigured(f"Cannot import renderer class '{renderer_class_path}': {e}")

    # Extract configuration options
    renderer_kwargs = renderer_config.get("config", {}) or {}
    renderer_icons = renderer_config.get("icons", {}) or {}

    # Create instance
    try:
        renderer_instance = renderer_class(
            icons=renderer_icons,
            **renderer_kwargs,
        )
    except Exception as e:
        raise ImproperlyConfigured(f"Cannot instantiate renderer '{name}' with class '{renderer_class_path}': {e}")

    # Cache the instance
    _renderer_cache[name] = renderer_instance
    return renderer_instance


def clear_cache() -> None:
    """Clear renderer cache.

    Useful for testing and development when settings might change.
    """
    _renderer_cache.clear()


def icon(name: str, renderer: str = "default", **kwargs: Any) -> SafeString:
    """Render an icon using the specified or default renderer.

    Args:
        name: The icon name to render
        renderer: Name of the renderer to use (defaults to 'default')
        **kwargs: Additional attributes for the icon

    Returns:
        Safe HTML string containing the rendered icon
    """
    renderer_instance = get_renderer(renderer)
    return cast(SafeString, renderer_instance(name, **kwargs))
