from kombu import Exchange, Queue
from flished import settings
from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flished.settings')
app = Celery(settings.SITE_NAME)
app.config_from_object('django.conf:settings', namespace=settings.CELERY_NAMESPACE)
app.conf.task_queues = (
    Queue(settings.CELERY_DEFAULT_QUEUE, Exchange(settings.CELERY_DEFAULT_EXCHANGE), routing_key=settings.CELERY_DEFAULT_ROUTING_KEY),
    Queue(settings.CELERY_OUTGOING_MAIL_QUEUE, Exchange(settings.CELERY_OUTGOING_MAIL_EXCHANGE), routing_key=settings.CELERY_OUTGOING_MAIL_ROUTING_KEY),
    Queue(settings.CELERY_IDENTIFICATION_QUEUE, Exchange(settings.CELERY_IDENTIFICATION_EXCHANGE), routing_key=settings.CELERY_IDENTIFICATION_ROUTING_KEY),
    Queue(settings.CELERY_LOGGER_QUEUE, Exchange(settings.CELERY_LOGGER_EXCHANGE), routing_key=settings.CELERY_LOGGER_ROUTING_KEY),
)
app.conf.task_default_queue = settings.CELERY_DEFAULT_QUEUE
app.conf.task_default_exchange_type = settings.CELERY_DEFAULT_EXCHANGE_TYPE
app.conf.task_default_routing_key = settings.CELERY_DEFAULT_ROUTING_KEY
app.conf.beat_schedule = {
    'clean_users': {
        'task': 'core.tasks.clean_users_not_actif',
        'schedule' : crontab(minute=0, hour=0)

    },
    'scheduled_posts': {
        'task': 'blog.tasks.publish_scheduled_posts',
        'schedule' : crontab(minute="*/15", hour="*")

    },
}
app.autodiscover_tasks()