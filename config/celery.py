"""
Celery app: reads CELERY_* settings, autodiscovers tasks.py in every app, defines the Beat schedule.

Built in: Level 6
"""

# TODO: app = Celery('config')
# TODO: app.config_from_object('django.conf:settings', namespace='CELERY')
# TODO: app.autodiscover_tasks()
# TODO: beat_schedule: run apps.tracker.tasks.send_follow_up_reminders daily at 09:00
