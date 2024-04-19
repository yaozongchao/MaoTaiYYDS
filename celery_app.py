from celery import Celery
from main import *

app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task
def imaotai_task():
    print("Task executed at 09:00:05 AM every day")
    main_task()