from django.apps import AppConfig


class TourappsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tourApps'

    def ready(self):
        import tourApps.signals
