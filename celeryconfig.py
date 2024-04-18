from datetime import time
from celery.schedules import crontab

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_TIMEZONE_UTC = False
CELERYBEAT_SCHEDULE = {
    'execute-my-task-every-day-at-09-00-05-am': {
        'task': 'tasks.repeat_task',
        'schedule': crontab(hour=9, minute=0, second=5),
    },
}