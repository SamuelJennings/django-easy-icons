"""Tests for template tags."""

from unittest.mock import patch

from django.template import Context, Template
from django.test import override_settings
from django.utils.safestring import SafeString

from easy_icons.templatetags.easy_icons import icon


class TestIconTemplateTag:
    """Test cases for the icon template tag."""

    def test_icon_tag_basic(self):
        """Test basic icon template tag usage."""
        config = {
            "default": {
                "renderer": "easy_icons.renderers.ProviderRenderer",
                "config": {"tag": "i"},
                "icons": {"home": "fa-home"}
            }
        }
        
        with override_settings(EASY_ICONS=config):
            result = icon("home")
            
            assert isinstance(result, SafeString)
            assert '<i class="fa-home"' in result

    def test_icon_tag_with_renderer(self):
        """Test icon template tag with explicit renderer."""
        config = {
            "default": {
                "renderer": "easy_icons.renderers.SvgRenderer",
                "config": {"svg_dir": "icons"},
                "icons": {"home": "home.svg"}
            },
            "fontawesome": {
                "renderer": "easy_icons.renderers.ProviderRenderer",
                "config": {"tag": "i"},
                "icons": {"heart": "fa-heart"}
            }
        }
        
        with override_settings(EASY_ICONS=config):
            result = icon("heart", renderer="fontawesome")
            
            assert isinstance(result, SafeString)
            assert '<i class="fa-heart"' in result

    def test_icon_tag_with_attributes(self):
        """Test icon template tag with additional attributes."""
        config = {
            "default": {
                "renderer": "easy_icons.renderers.ProviderRenderer",
                "config": {"tag": "i"},
                "icons": {"star": "fa-star"}
            }
        }
        
        with override_settings(EASY_ICONS=config):
            result = icon("star", **{"class": "large", "data-role": "button"})
            
            # May have separate class attributes
            assert 'fa-star' in result and 'large' in result
            assert 'data-role="button"' in result

    def test_icon_tag_in_template(self):
        """Test icon template tag within Django template."""
        config = {
            "default": {
                "renderer": "easy_icons.renderers.ProviderRenderer",
                "config": {"tag": "span"},
                "icons": {"bookmark": "fa-bookmark"}
            }
        }
        
        template_content = "{% load easy_icons %}{% icon 'bookmark' %}"
        
        with override_settings(EASY_ICONS=config):
            template = Template(template_content)
            result = template.render(Context())
            
            assert '<span class="fa-bookmark"' in result

    def test_icon_tag_in_template_with_variables(self):
        """Test icon template tag with template variables."""
        config = {
            "default": {
                "renderer": "easy_icons.renderers.ProviderRenderer",
                "config": {"tag": "i"},
                "icons": {"user": "fa-user", "admin": "fa-user-shield"}
            }
        }
        
        template_content = "{% load easy_icons %}{% icon icon_name class=css_class %}"
        
        with override_settings(EASY_ICONS=config):
            template = Template(template_content)
            context = Context({"icon_name": "user", "css_class": "active"})
            result = template.render(context)
            
            assert 'class="fa-user active"' in result

    def test_icon_tag_with_quoted_attributes(self):
        """Test icon template tag with quoted attribute values."""
        config = {
            "default": {
                "renderer": "easy_icons.renderers.ProviderRenderer",
                "config": {"tag": "i"},
                "icons": {"settings": "fa-cog"}
            }
        }
        
        template_content = """{% load easy_icons %}{% icon 'settings' class="gear large" title="Settings Menu" %}"""
        
        with override_settings(EASY_ICONS=config):
            template = Template(template_content)
            result = template.render(Context())
            
            assert 'class="fa-cog gear large"' in result
            assert 'title="Settings Menu"' in result

    def test_icon_tag_with_renderer_parameter(self):
        """Test icon template tag with renderer parameter in template."""
        config = {
            "svg": {
                "renderer": "easy_icons.renderers.SvgRenderer",
                "config": {"svg_dir": "icons"},
                "icons": {"home": "home.svg"}
            },
            "fontawesome": {
                "renderer": "easy_icons.renderers.ProviderRenderer",
                "config": {"tag": "i"},
                "icons": {"home": "fa-home"}
            }
        }
        
        template_content = "{% load easy_icons %}{% icon 'home' renderer='fontawesome' %}"
        
        with override_settings(EASY_ICONS=config):
            with patch('easy_icons.renderers.render_to_string') as mock_render:
                mock_render.return_value = '<svg><path d="M0 0L10 10"/></svg>'
                
                template = Template(template_content)
                result = template.render(Context())
                
                assert '<i class="fa-home"' in result

    def test_icon_tag_default_renderer_parameter(self):
        """Test that icon template tag defaults to 'default' renderer."""
        config = {
            "default": {
                "renderer": "easy_icons.renderers.ProviderRenderer",
                "config": {"tag": "i"},
                "icons": {"heart": "fa-heart"}
            }
        }
        
        # Test both function call and template usage
        with override_settings(EASY_ICONS=config):
            # Direct function call
            result1 = icon("heart")
            assert '<i class="fa-heart"' in result1
            
            # Template usage
            template_content = "{% load easy_icons %}{% icon 'heart' %}"
            template = Template(template_content)
            result2 = template.render(Context())
            assert '<i class="fa-heart"' in result2

    def test_icon_tag_with_boolean_attributes(self):
        """Test icon template tag with boolean attributes."""
        config = {
            "default": {
                "renderer": "easy_icons.renderers.ProviderRenderer",
                "config": {"tag": "i"},
                "icons": {"check": "fa-check"}
            }
        }
        
        template_content = "{% load easy_icons %}{% icon 'check' hidden=True disabled=False %}"
        
        with override_settings(EASY_ICONS=config):
            template = Template(template_content)
            result = template.render(Context())
            
            # Django's flatatt handles boolean attributes - True values show as just the attribute name
            assert 'hidden' in result
            assert 'disabled' not in result or 'disabled=""' in result

    def test_icon_tag_with_context_variables(self):
        """Test icon template tag with various context variable types."""
        config = {
            "default": {
                "renderer": "easy_icons.renderers.ProviderRenderer",
                "config": {"tag": "i"},
                "icons": {"arrow": "fa-arrow"}
            }
        }
        
        template_content = "{% load easy_icons %}{% icon 'arrow' width=size height=size class=classes %}"
        
        with override_settings(EASY_ICONS=config):
            template = Template(template_content)
            context = Context({
                "size": "24",
                "classes": "rotate-90 blue"
            })
            result = template.render(context)
            
            assert 'width="24"' in result
            assert 'height="24"' in result
            assert 'class="fa-arrow rotate-90 blue"' in result

    def test_icon_tag_loads_correctly(self):
        """Test that the easy_icons templatetags library loads correctly."""
        template_content = "{% load easy_icons %}Loaded successfully"
        
        template = Template(template_content)
        result = template.render(Context())
        
        assert "Loaded successfully" in result

    def test_icon_tag_multiple_in_template(self):
        """Test multiple icon tags in same template."""
        config = {
            "default": {
                "renderer": "easy_icons.renderers.ProviderRenderer",
                "config": {"tag": "i"},
                "icons": {
                    "home": "fa-home",
                    "user": "fa-user",
                    "settings": "fa-cog"
                }
            }
        }
        
        template_content = """
        {% load easy_icons %}
        {% icon 'home' class='nav' %}
        {% icon 'user' class='profile' %}
        {% icon 'settings' class='admin' %}
        """
        
        with override_settings(EASY_ICONS=config):
            template = Template(template_content)
            result = template.render(Context())
            
            assert 'class="fa-home nav"' in result
            assert 'class="fa-user profile"' in result
            assert 'class="fa-cog admin"' in result
