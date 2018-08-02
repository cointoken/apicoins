from celery import Celery
from celery.utils.log import get_task_logger
from tasks import app


logger = get_task_logger(__name__)


@app.task
def getaddress(name,amount):
    addresses = {name:[]}
    for i in amount:
        addresses[name].append()
    return addresses
