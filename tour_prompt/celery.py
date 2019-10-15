import os

from celery import Celery

app = Celery('tour_celery',
             broker=os.environ.get('CELERY_BROKER_URL'),
             backend=os.environ.get('CELERY_RESULT_BACKEND'),
             )
# include=['proj.tasks']

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)
