from datetime import timedelta
from celery.schedules import crontab

broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/1'

timezone = 'Asia/Shanghai'
enable_utc = False

beat_schedule = {
    'imaotai_task': {
        'task': 'celery_app.imaotai_task',
        'schedule': crontab(minute=20, hour=9),
        'args': (),
    },
}