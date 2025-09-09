#!/usr/bin/env python

import os
import sys

if __name__ == "__main__":
    # Add src directory to Python path so easy_icons can be imported
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
