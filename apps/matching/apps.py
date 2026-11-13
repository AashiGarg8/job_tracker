from django.apps import AppConfig


class MatchingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.matching"   # full dotted path because the app lives inside apps/
    label = "matching"        # short name used in migrations and AUTH_USER_MODEL
