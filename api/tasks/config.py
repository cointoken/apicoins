# -*- coding:utf-8 -*-
from kombu import Queue
from datetime import timedelta
from celery.schedules import crontab


REDIS_URL = 'redis://0.0.0.0:6379'
BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_IMPORTS = ('tasks.task_get_address')
CELERYD_MAX_TASKS_PER_CHILD = 40

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': '',
        'schedule': timedelta(seconds = 30),
        'args': ()
    },
    'multiply-at-some-time': {
        'task': '',
        'schedule': crontab(hour=10,minute=10),
        'args': (3,7)
    }
}

CELERY_QUEUES = (
    Queue('btc',routing_key = 'task.btc'),
    Queue('ltc',routing_key = 'task.ltc'),
    Queue('bch',routing_key = 'task.bch'),
    Queue('usdt',routing_key = 'task.usdt'),
    Queue('eth',routing_key = 'task.eth'),
    Queue('etc',routing_key = 'task.eth')
)
