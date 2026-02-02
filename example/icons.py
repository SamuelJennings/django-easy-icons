"""Example icon packs for third-party package integration.

Third-party packages can define icon packs as dictionaries and reference them
in their documentation for users to include via the 'packs' configuration key.

Usage Example:
--------------
A third-party Django package (e.g., "mypackage") can define icon packs in a
module like mypackage/icons.py:

    # mypackage/icons.py
    FONTAWESOME = {
        "action-edit": "fa-edit",
        "action-delete": "fa-trash",
        "status-success": "fa-check",
        "status-error": "fa-times",
    }

    BOOTSTRAP = {
        "action-edit": "bi-pencil",
        "action-delete": "bi-trash",
        "status-success": "bi-check",
        "status-error": "bi-x",
    }

Then in your package's documentation, instruct users to add the pack to their
EASY_ICONS configuration:

    # settings.py
    EASY_ICONS = {
        "fontawesome": {
            "renderer": "easy_icons.renderers.ProviderRenderer",
            "config": {"tag": "i"},
            "packs": [
                "mypackage.icons.FONTAWESOME",  # Add your third-party pack
            ],
            "icons": {
                # Users can override specific icons here if needed
            },
        }
    }

Key Features:
-------------
- Multiple packs can be listed; later packs override earlier ones (last-wins)
- Explicit "icons" entries always override pack definitions
- Invalid or missing packs log warnings but don't break the application
- Packs must be dictionaries mapping icon names to icon identifiers

Benefits:
---------
- No manual copy/paste of icon definitions needed
- Third-party packages can update icons without requiring user changes
- Users maintain control via explicit icon overrides
- Multiple icon set variants supported (FontAwesome, Bootstrap Icons, etc.)
"""

# Example pack for SVG renderer
SVG = {
    "home": "home.svg",
    "user": "user.svg",
}

# Example pack for FontAwesome (ProviderRenderer)
FONTAWESOME = {
    "heart": "fa fa-heart",
}
