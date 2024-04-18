from celery import Celery
from main import *

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def imaotai_task():
    print("Task executed at 09:00:05 AM every day")
    main_task()
    
    
@app.task
def repeat_task():
    for i in range(10):
        imaotai_task.apply_async(countdown=2 * i)