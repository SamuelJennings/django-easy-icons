# Django Easy Icons
A consistent, pythonic interface for the management of icons in Django 

Django Easy Icons provides a consistent, pythonic interface for the management of icons in Django across your project and any 3rd party apps you rely on.

Django Easy Icons is a simple app that makes it super easy to manage your applications icons using your tool of choice. Declare your icons in your templates using the {% icon %} template tag and easily customize attrs using keyword arguments. 


Because `django-easy-icons` is not locked in to any one icon library, you can safely add icons to reusable apps while still allowing users to display icons using their method of choice.


## Installation

```
pip install django-easy-icons
```

Then add `easy_icons` to your `INSTALLED_APPS` in `settings.py`

```python
INSTALLED_APPS = [
    ...
    'easy_icons',
    ...
]
```

## Basic Usage 

### In templates

Use the `icon` template tag in your templates to reference icons in a consistent way across your site. The first argument is the name of the icon you wish to render. You can also supply keyword arguments to customize the icon's attributes.

```django
{% load easy_icons %}

<button>{% icon 'home' id="home" class="text-primary" %}Go home</button>
```

### In python code

To use icons in python code, simply import the `icon` template tag and use it as a function.

```python
from django.views.generic import TemplateView
from easy_icons import icon

class HomeView(TemplateView):
    template_name = 'home.html'
    extra_context = {'home_icon': icon('home', id="home", width="45px")}
```

## Available renderers

`django-easy-icons` comes with 3 options for rendering icons in your project. Specify which renderer you wish to use in your `settings.py` file.

```python
EASY_ICONS = {
    # "default_renderer": "svg", # for embedded SVG icons
    # "default_renderer": "sprites", # for SVG sprites in a single, external file
    "default_renderer": "provider", # default, for css/js libraries like Font Awesome
}
```

### Embedded SVG icons

The `easy_icons.renderers.svg` renderer uses Django's template loader to embed SVG icons directly into your html markup. By default, this renderer searches for icons in the `icons/` template directory. Because it uses the Django template engine, you can easily override icons in external apps by placing your own icons in the same directory.

```python
EASY_ICONS = {
    "default_renderer": "svg",
}
```
Place icons in your `templates` directory like so:

```bash
your_app/
    templates/
        icons/
            home.svg
            ...
```

Keywords are included as attributes of the svg tag. Any pre-existing attributes are preserved.

```django
<button>{% icon 'home' height="1rem" %}Go home</button>

<!-- rendered output -->
<button>
    <svg height="1rem" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 12"> ... </svg>
    Go home
</button>
```


### Using an external provider (e.g. CSS or JS library)

`easy_icons.renderers.provider` allows you to use an external CSS or JS library to render your icons. This is useful when you want to use a popular icon library like Font Awesome or Material Icons.

External packages (e.g. Font Awesome) typically use a class to render icons. Therefore, this renderer simply includes an empty tag with the specified class. You can control the tag used by setting the `tag` attribute in your `settings.py` file. By default, the `i` tag. You also need to specify a `classmap` that maps icon names to classes expected by your preferred icon provider.

```python

EASY_ICONS = {
    "default_renderer": "provider",
    "tag": "i", # default
    "classmap": {
        # maps named icons to classes (for use with icon providers like Font Awesome)
        "home": "fas fa-home",
    }
}
```

```django
<button>{% icon 'home' class="text-primary" title="Go home" %}Go home</button>

<!-- rendered output -->
<button>
    <i class="fas fa-home text-primary" title="Go home"></i>
    Go home
</button>
```

Note: Remember to include any necessary CSS or JS files in your template to render the icons correctly.

### SVG sprites

Sprites are a way to include multiple icons in a single file. This can reduce the number of requests made to the server and improve performance. The `easy_icons.renderers.sprites` renderer allows you to use a sprite sheet to render your icons. You can specify the URL to the sprite sheet in your `settings.py` file.

```python
from django.conf.urls.static import static

EASY_ICONS = {
    "default_renderer": "sprites",
    "sprite_url": static("path/to/bootstrap-icons.svg"),
}
```

```django
<button>{% icon 'home' %}Go home</button>

<!-- rendered output -->
<button>
    <svg>
        <use xlink:href="/path/to/bootstrap-icons.svg#home" />
    </svg>
    Go home
</button>
```

WARNING: Chromium browsers [have a bug](https://issues.chromium.org/issues/41164645) that prevents cross-domain requests on the <use> element. In order for sprites to work on these browsers, you must self-host the sprite sheet on the same domain as your website.

### Custom renderers

If none of the provided options suit your needs, you can easily create your own renderer. Simply define a function that takes an icon name and any kwargs provided on declaration. The function should return a safe string that represents the rendered icon as html. 

```python
from easy_icons.renderers import _attrs

# myapp/utils.py
def custom_renderer(icon_name, **kwargs):
    # passing kwargs to _attrs will ensure the `defaults` directive is respected and convert 
    # everything to a string using `django.forms.utils.flatatt`.
    attrs = _attrs(kwargs)
    return f"<div><span class='{icon_name}' {attrs} /></div>"

# settings.py
EASY_ICONS = {
    "renderers": {
        "custom": "myapp.utils.custom_renderer",
        # declaring renderers will override easy-icons defaults so remember to 
        # include any other renderers you wish to use
        "svg": "easy_icons.renderers.svg", 
        
    },
    # set the default renderer to your custom renderer
    "default_renderer": "custom",
}
```

## Default attributes

No matter which renderer you choose, it is often necessary to provide default attributes across all of your icons in a single project. This is particularly useful to maintain a consistent look and feel across your site. You can easily do this by setting the `attrs` attribute in your `settings.py` file.

```python
EASY_ICONS = {
    "renderer": "easy_icons.renderers.svg",
    "attrs": {
        "height": "16px",
        "fill": "currentColor",
    }
}
```

Now, embedded SVG icons will include the height and fill attributes by default.

```django
<button>{% icon 'home' %}Go home</button>

<!-- rendered output -->
<button>
    <svg height="16px" fill="currentColor"> ... </svg>
    Go home
</button>
```

Override default attrs by providing identical keyword arguments to the `icon` template tag.

```django
<button>{% icon 'home' height="64px" width="64px" fill="green" %}Go home</button>

<!-- rendered output -->
<button>
    <svg height="64px" width="64px" fill="green"> ... </svg>
    Go home
</button>
```

You can prevent default attrs from being applied without overriding by passing the `defaults=False` keyword argument to the `icon` template tag.

```django
<button>{% icon 'home' defaults=False class="extra-large-icon" %}Go home</button>

<!-- rendered output -->
<button>
    <svg class="extra-large-icon"> ... </svg>
    Go home
</button>
```

## Icon naming and aliases

Sometimes, you may find yourself in a situgation where the same icon should apply to multiple icon names. You can list each item out individually in your `classmap`, however, a more robust solution is to use aliases.

Using aliases reduces clutter and is especially helpful when using embedded svg icons so you don't need to copy and past the same icon with different names into your icons dir. 

```python
EASY_ICONS = {
    "renderer": "easy_icons.renderers.svg",
    "aliases": {
        "pencil": "edit",
        "update": "edit",
    },
    "classmap": {
        "edit": "fas fa-pencil",
    },
}
```
```django
<!-- appA/detail.html -->
{% icon 'pencil' %}
<!-- appB/detail.html -->
{% icon 'update' %}
<!-- appC/detail.html -->
{% icon 'edit' %}

<!-- rendered output across all apps using aliases -->
<i class="fas fa-pencil"></i>
```


## Overriding the default renderer

Sometimes it is usefuly to override the default renderer for a single icon declaration. You can do this by passing the `renderer` keyword argument to the `icon` template tag.

```django
<div class="full-page-icon">  
    {% icon 'home' renderer="svg" height="100%" width="100%" %}
</div>
```

## Default configuration

The following are the default settings for `django-easy-icons`. You can override these in your `settings.py` file to customize how icons are rendered in your templates.

```python

# default settings for django-easy-icons
EASY_ICONS = {
    # all renderers available to the user
    "renderers": {
        "provider": "easy_icons.renderers.provider",
        "sprites": "easy_icons.renderers.sprites",
        "svg": "easy_icons.renderers.svg",
    },
    # the default renderer used to render an icon in your template
    "default_renderer": "provider",
    # default attributes applied to all icons
    "attrs": {},
    # maps aliases to icon names
    "aliases": {},
    # maps named icons to classes (for use with libraries like Font Awesome)
    "classmap": {},
    # default tag for css/js packages (only applicable when using 'easy_icons.renderers.external_package')
    "tag": "i",
    # directory where SVG icons are stored (only applicable when using 'easy_icons.renderers.svg')
    "svg_dir": "icons",
    # URL to an external sprite sheet (only applicable when using 'easy_icons.renderers.sprites')
    "sprite_url": None,

}
```
