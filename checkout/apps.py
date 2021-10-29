from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

# From Code Institute Boutique Ado tutorial
class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals    