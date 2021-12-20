"""
This is example of docstring which is mandatory for any app in django.
"""
from django.apps import AppConfig


class CleanCodeConfig(AppConfig):
    """
    clean code app config
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "clean_code"
