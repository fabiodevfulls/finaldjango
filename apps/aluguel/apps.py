from django.apps import AppConfig




class AluguelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.aluguel'

    def ready(self):
        import apps.aluguel.signals
