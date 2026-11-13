from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.accounts"   # full dotted path because the app lives inside apps/
    label = "accounts"        # short name used in migrations and AUTH_USER_MODEL
