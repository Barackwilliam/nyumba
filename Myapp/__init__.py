
default_app_config = 'Myapp.apps.MyappConfig'  # Capital M
# And in AppConfig:
from django.apps import AppConfig

class MyappConfig(AppConfig):
    name = 'Myapp'

    def ready(self):
        import Myapp.translation
