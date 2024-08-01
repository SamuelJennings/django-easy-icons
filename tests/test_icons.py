import os

from django.conf import settings
from django.template import Template, TemplateDoesNotExist
from django.template.context import Context
from django.test.testcases import SimpleTestCase

from easy_icons.templatetags.easy_icons import icon


class IconTagTest(SimpleTestCase):

    def test_renders_svg(self):
        svg = icon("home")
        assert svg.startswith("<svg")

        svg = icon("home.svg")
        assert svg.startswith("<svg")

    def test_svg_renders_with_defaults(self):
        svg = icon("home")
        self.assertIn('height="1em"', svg)
        self.assertIn('fill="currentColor"', svg)

    def test_svg_renders_with_custom_defaults(self):
        with self.settings(easy_icons_DEFAULTS={"height": "2em", "fill": "red"}):
            svg = icon("home")
            self.assertIn('height="2em"', svg)
            self.assertIn('fill="red"', svg)

    def test_svg_renders_with_custom_attributes(self):
        svg = icon("home", height="2em", fill="red")
        self.assertIn('height="2em"', svg)
        self.assertIn('fill="red"', svg)

        # make sure the defaults are not present
        self.assertNotIn('height="1em"', svg)
        self.assertNotIn('fill="currentColor"', svg)

    def test_missing_icon_raises_error(self):
        with self.assertRaises(TemplateDoesNotExist):
            icon("missing")

    def test_alternative_directory_setting(self):
        with self.settings(easy_icons_ICONS_DIR="alt_dir"):
            svg = icon("alt_dir")
            self.assertIn('height="1em"', svg)
        
            with self.assertRaises(TemplateDoesNotExist):
                icon("home")

    def test_render_without_defaults(self):
        svg_file = open(os.path.join(settings.BASE_DIR, 'tests', "example","templates","icons", 'home.svg')).read()

        self.assertEqual(icon("home", nodefaults=True), svg_file)

    def test_when_given_invalid_file_it_should_fail_silently(self):
        svg = icon("home")
        template = Template("{% load easy_icons %}{% icon 'home' %}")
        self.assertEqual(svg, template.render(Context()))
        self.assertEqual(svg, template.render(Context()))
        self.assertEqual(svg, template.render(Context()))
