from django.apps import AppConfig
import os


class AutomationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'automation'

    def ready(self):
        if os.environ.get("RUN_MAIN"):
            print("We have fully loaded automation app")
            from . import factories
