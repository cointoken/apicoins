import requests
import json
from tasks import worker,create_engine,datetime

import sys
sys.path.append('..')
from dbs.models import  Deposits
from dbs.crud import CRUD
import config


def now_time():
    return datetime.now().strftime('%Y-%m-%d')


@worker.task
def import_deposits():
    deposit_url = 'http://192.168.1.143:3000/admin/success_deposits?begin_time={0}&end_time={1}'.format(now_time(),now_time())
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    crud = CRUD(engine)

    r = requests.get(deposit_url)
    j = json.loads(r.content)
    if j:
        try:
            if j['status']==200 and j['message']=='success':
                datas = j['data']
                
                for d in datas:
                    de = Deposits(d['id'],d['currency'],d['email'],d['phone_number'],float(d['amount']),float(d['fee']),d['fund_uid'],datetime.strptime(d['created_at'],'%Y-%m-%d %H:%M:%S'))
                    crud.deposits_insert(de)
        except:
            crud.close()
    crud.close()





