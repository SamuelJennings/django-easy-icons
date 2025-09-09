# Renderers

Django Easy Icons provides three built-in renderer classes that handle different types of icon sources. Each renderer has its own configuration options and use cases.

## Overview

All renderers share the same basic interface but handle different icon sources:

- **SvgRenderer**: Renders SVG files from your Django templates directory
- **ProviderRenderer**: Renders font icons using CSS classes (Font Awesome, Bootstrap Icons, etc.)
- **SpritesRenderer**: Renders icons from SVG sprite files using `<use>` elements

## Renderer Configuration

Each renderer is configured in your Django settings using this structure:

```python
# settings.py
EASY_ICONS = {
    "renderer_name": {
        "renderer": "easy_icons.renderers.RendererClass",
        "config": {
            # Renderer-specific options
        },
        "icons": {
            "icon_name": "icon_identifier",
        }
    }
}
```

## Built-in Renderers

### SvgRenderer

The `SvgRenderer` loads SVG files from your Django templates directory and embeds them directly into your HTML. This is ideal for custom icons or when you want to style SVG elements directly with CSS.

**Class**: `easy_icons.renderers.SvgRenderer`

**How it works**: 
1. Looks for SVG files in the specified template directory
2. Loads the SVG content using Django's template loader
3. Merges any provided attributes with the SVG's root `<svg>` element
4. Returns the complete SVG markup

**Configuration**:

```python
EASY_ICONS = {
    "default": {
        "renderer": "easy_icons.renderers.SvgRenderer",
        "config": {
            "svg_dir": "icons",  # Template directory containing SVG files
            "default_attrs": {   # Optional: default attributes for all SVGs
                "height": "1em",
                "fill": "currentColor",
                "class": "icon"
            }
        },
        "icons": {
            "home": "home.svg",
            "user": "user.svg", 
            "settings": "gear.svg"
        }
    }
}
```

**Configuration Options**:

- `svg_dir`: Template directory where SVG files are stored (relative to your template directories)
- `default_attrs`: Optional dictionary of HTML attributes applied to all SVG elements

**Usage**:

```django
{% load easy_icons %}

<!-- Basic usage -->
{% icon "home" %}

<!-- With custom attributes -->
{% icon "home" class="nav-icon" width="24" height="24" %}
```

### ProviderRenderer

The `ProviderRenderer` generates HTML elements with CSS classes for icon font libraries like Font Awesome, Bootstrap Icons, or any CSS-based icon system.

**Class**: `easy_icons.renderers.ProviderRenderer`

**How it works**:

1. Creates an HTML element (usually `<i>` or `<span>`) 
2. Sets the `class` attribute to the icon's CSS classes
3. Merges any additional attributes you provide
4. Returns the complete HTML element

**Configuration**:

```python
EASY_ICONS = {
    "fontawesome": {
        "renderer": "easy_icons.renderers.ProviderRenderer",
        "config": {
            "tag": "i"  # HTML tag to use (default: "i")
        },
        "icons": {
            "home": "fas fa-home",
            "user": "fas fa-user", 
            "heart": "fas fa-heart",
            "settings": "fas fa-cog"
        }
    }
}
```

**Configuration Options**:

- `tag`: HTML tag to use for icons (default: `"i"`, commonly `"span"` is also used)

**Usage**:

```django
{% load easy_icons %}

<!-- Basic usage -->
{% icon "home" renderer="fontawesome" %}

<!-- With custom attributes -->
{% icon "heart" renderer="fontawesome" class="text-red fs-4" title="Favorite" %}
```

**Output Example**:
```html
<i class="fas fa-home"></i>
<i class="fas fa-heart text-red fs-4" title="Favorite"></i>
```

### SpritesRenderer

The `SpritesRenderer` generates SVG elements that reference symbols in an external SVG sprite file using `<use>` elements. This is efficient for large icon sets as the sprite file can be cached by the browser.

**Class**: `easy_icons.renderers.SpritesRenderer`

**How it works**:

1. Creates an `<svg>` element with a nested `<use>` element
2. Sets the `<use>` element's `href` attribute to point to the sprite symbol
3. Merges any provided attributes with the SVG element  
4. Returns the complete SVG markup

**Configuration**:

```python
EASY_ICONS = {
    "sprites": {
        "renderer": "easy_icons.renderers.SpritesRenderer", 
        "config": {
            "sprite_url": "/static/icons/bootstrap-icons.svg"  # Path to sprite file
        },
        "icons": {
            "home": "house",           # Symbol ID in the sprite
            "user": "person-circle",   # Symbol ID in the sprite
            "search": "search",
            "menu": "list"
        }
    }
}
```

**Configuration Options**:

- `sprite_url`: URL path to the SVG sprite file (relative to your domain)

**Usage**:

```django
{% load easy_icons %}

<!-- Basic usage -->
{% icon "home" renderer="sprites" %}

<!-- With custom attributes -->
{% icon "search" renderer="sprites" width="20" height="20" class="search-icon" %}
```

**Output Example**:
```html
<svg><use href="/static/icons/bootstrap-icons.svg#house"></use></svg>
<svg width="20" height="20" class="search-icon"><use href="/static/icons/bootstrap-icons.svg#search"></use></svg>
```

## Using Multiple Renderers

You can configure multiple renderers simultaneously and choose which one to use for each icon. The first renderer defined becomes the "default" renderer used when no specific renderer is specified.

### Complete Example

Here's a comprehensive example using all three renderer types:

```python
# settings.py
EASY_ICONS = {
    # Default renderer - used when no renderer specified
    "default": {
        "renderer": "easy_icons.renderers.SvgRenderer",
        "config": {
            "svg_dir": "icons",
            "default_attrs": {
                "height": "1em",
                "fill": "currentColor"
            }
        },
        "icons": {
            "logo": "company-logo.svg",
            "custom-icon": "my-icon.svg"
        }
    },
    
    # Font Awesome for common UI icons
    "fontawesome": {
        "renderer": "easy_icons.renderers.ProviderRenderer",
        "config": {
            "tag": "i"
        },
        "icons": {
            "home": "fas fa-home",
            "user": "fas fa-user", 
            "settings": "fas fa-cog",
            "edit": "fas fa-edit",
            "delete": "fas fa-trash"
        }
    },
    
    # Bootstrap Icons sprite for comprehensive icon set  
    "bootstrap": {
        "renderer": "easy_icons.renderers.SpritesRenderer",
        "config": {
            "sprite_url": "/static/bootstrap-icons.svg"
        },
        "icons": {
            "heart": "heart",
            "star": "star", 
            "arrow-left": "arrow-left",
            "arrow-right": "arrow-right"
        }
    }
}
```

### Using Multiple Renderers in Templates

Once configured, you can use icons from different renderers by specifying the renderer name:

```django
{% load easy_icons %}

<!-- Uses default renderer (SVG) -->
{% icon "logo" %}

<!-- Uses Font Awesome renderer -->
{% icon "home" renderer="fontawesome" %}

<!-- Uses Bootstrap Icons sprite renderer -->
{% icon "heart" renderer="bootstrap" %}

<!-- All renderers support custom attributes -->
{% icon "user" renderer="fontawesome" class="nav-icon text-primary" %}
{% icon "star" renderer="bootstrap" width="24" height="24" class="favorite" %}
```

### Choosing the Right Renderer

**Use SvgRenderer when**:
- You have custom/branded icons
- You need to style individual SVG elements with CSS
- You have a small number of icons
- You want maximum control over the SVG markup

**Use ProviderRenderer when**:
- You're using established icon fonts (Font Awesome, Bootstrap Icons, etc.)
- You want simple implementation with CSS classes
- You need icons that scale well with text
- Performance is important (font icons are cached by browsers)

**Use SpritesRenderer when**:
- You have a large number of icons
- You want the benefits of SVG with efficient caching
- You're using icon libraries that provide sprite files
- You need both performance and SVG flexibility

### Renderer-Specific Tips

**SvgRenderer Tips**:
- Organize SVG files in subdirectories within your `svg_dir` for better organization
- Use consistent `viewBox` attributes across your SVG files for predictable sizing
- Set `fill="currentColor"` in your SVG files to inherit text color automatically

**ProviderRenderer Tips**:
- Different icon fonts may use different CSS class patterns (e.g., `fas fa-home` vs `bi bi-house`)
- Make sure to include the appropriate CSS/font files in your templates
- Consider using different renderer names for different icon libraries

**SpritesRenderer Tips**:
- Ensure your sprite file is accessible at the configured URL
- Symbol IDs in the sprite must match the values in your icons configuration
- Consider using CDN-hosted sprites for better caching and performance

### Icon Naming Best Practices

Use semantic names that describe the icon's purpose rather than its appearance:

```python
"icons": {
    # ✅ Good - semantic names
    "home": "fas fa-home",
    "edit": "fas fa-pencil", 
    "delete": "fas fa-trash",
    "save": "fas fa-check",
    
    # ❌ Avoid - appearance-based names
    "pencil": "fas fa-pencil",
    "trash": "fas fa-trash", 
    "checkmark": "fas fa-check"
}
```

This approach makes your templates more maintainable and allows you to change the actual icon without updating template code.

## Default Attributes

All renderers support `default_attrs` in their configuration to set attributes that apply to all icons:

```python
"config": {
    "default_attrs": {
        "class": "icon",
        "height": "1em", 
        "aria-hidden": "true"
    }
}
```

Template tag attributes completely override default attributes - they don't merge.

## Summary

Django Easy Icons provides three powerful renderer classes:

- **SvgRenderer**: Best for custom icons and maximum SVG control
- **ProviderRenderer**: Best for icon fonts and established icon libraries  
- **SpritesRenderer**: Best for large icon sets with efficient caching

You can use multiple renderers simultaneously to leverage the strengths of each approach in different parts of your application.
