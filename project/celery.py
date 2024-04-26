from celery.schedules import crontab
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')


app = Celery('project')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')


# Below is for illustration purposes. We
# configured so we can adjust scheduling
# in the Django admin to manage all
# Periodic Tasks like below
# app.conf.beat_schedule = {
#     'add-every-minute': {
#         'task': 'app.tasks.add_num',
#         'schedule': crontab(minute=1),
#     },
# }

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"request ")
