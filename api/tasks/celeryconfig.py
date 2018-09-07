from datetime import timedelta
from celery.schedules import crontab


BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_TIMEZONE='Asia/Shanghai'

CELERY_IMPORTS = (
    'tasks.task2'
)
#'tasks.task1'

CELERYBEAT_SCHEDULE = {
    'add-every-5-minutes': {
        'task': 'tasks.task2.get_ethereum_addresses',
        'schedule': timedelta(minutes=5),       # 每 5 分钟执行一次
        'args': ()
    }
    # },
    # 'add-every-20-minutes': {
    #      'task': 'tasks.task1.import_deposits',
    #      'schedule': timedelta(minutes=20),       # 每 20 分钟执行一次
    #      'args': ()
    # },
    # 'multiply-at-12-time': {
    #     'task': 'tasks.task.autotransfer',
    #     'schedule': crontab(hour=12, minute=00),   # 每天中午 12点 00分执行一次
    #     'args': ()                                 
    # }
}
