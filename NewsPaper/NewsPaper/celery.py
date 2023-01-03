import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper',)
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'weekly_sending',
        'schedule': crontab(hour=20, minute=5, day_of_week='monday'),
        'args': 'some_arg',
    },
}

app.autodiscover_tasks()
