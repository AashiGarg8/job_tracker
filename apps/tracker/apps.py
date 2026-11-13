from django.apps import AppConfig


class TrackerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.tracker"   # full dotted path because the app lives inside apps/
    label = "tracker"        # short name used in migrations and AUTH_USER_MODEL
