"""
Django settings for example project.

Generated by Cookiecutter Django Package
"""

import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


sys.path.append(str(BASE_DIR / "tests"))

SECRET_KEY = "=bodvqgkt@)emfe2!($i#1zd(x27@u!9*9+)^$8bu#sqsmm^*n"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "easy_icons",
    "example",
]


ROOT_URLCONF = "example.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
