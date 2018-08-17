from celery import Celery
from celery.utils.log import get_task_logger
from tasks import app
from ..coins.btc import Btc
from ..coins.eth import Eth
import json
import requests

logger = get_task_logger(__name__)


@app.task
def getaddress(name,amount):
    addresses = {name:[]}
    for i in amount:
        addresses[name].append()
    return addresses


def getdepositinfos():
    header = {"accept":""}
    params = {"":""}
    url='http://{0}'.format()
    r = requests.get(url,header=header,params=params)
    j = json.loads(r.content)
    arrs = 
    