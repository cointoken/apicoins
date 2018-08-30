
from __future__ import absolute_import
import unittest
import json
import re
from datetime import datetime
import requests
import json
import sys
sys.path.append('..')
from dbs.models import  Deposits
from dbs.crud import CRUD
import config

dic = {
  "": -0.04542530,
  "payment": 0.04597393
}
dic1 = {

}
def test_null():
    for key,value in dic1.items():
        if dic1[key] > 0.03:
            print(dic1[key],key)

def test_time():
    print(datetime.now().strftime('%Y-%m-%d'))


def now_time():
    return datetime.now().strftime('%Y-%m-%d')


def import_deposits():
    from sqlalchemy import create_engine
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    crud = CRUD(engine)
    eth_datas = crud.deposits_query_from_currency('btc')
    if len(eth_datas)>0:
        print(len(eth_datas))
    # datas = crud.deposits_query_from_currency('btc')
    # # print(len(datas))
    # # for d in datas:
    # #     print(d.deposit_id,d.currency,d.amount)


    # deposit_url = 'http://192.168.1.143:3000/admin/success_deposits?begin_time={0}&end_time={1}'.format('2018-08-06','2018-08-06')
    # # print(deposit_url)
    # r = requests.get(deposit_url)
    # j = json.loads(r.content)
    # if j:
    #     if j['status']==200 and j['message']=='success':
    #         datas = j['data']
                
    #         for d in datas:
    #             # print(d)
    #             de = Deposits(d['id'],d['currency'],d['email'],d['phone_number'],float(d['amount']),float(d['fee']),d['fund_uid'],datetime.strptime(d['created_at'],'%Y-%m-%d %H:%M:%S'))
    #             crud.deposits_insert(de)
    # crud.deposits_update_from_deposit_id(12,'1Pqd7NjttazdK4Pk8kfhL7XguhDgknSfjH','77ab80b2f6a08af8969692a9e856dc2563dbe4f08d16fb7ac0ced994053ab837')
    # txid = crud.deposits_query_from_address('447e8b88')
    # print(txid)


if __name__=='__main__':
    # result =  "bitcoincash:qr30v9s0l99zgfq802wkjsgylwx4l9aeush2yvvpye"
    # result = result[12:]
    # print(result)
    # reobj = re.match('^0x[a-fA-F0-9]{40}','0xeweioiqox12333')
    # result = {"valid_address": True} if reobj else {"valid_address": False}

    # r = "\"JSONDecodeError('Expecting value: line 1 column 1 (char 0)',)\""
    # r = r[:r.find('(')]
    # r = r[r.find("\"")+1:]
    # print(r)
    import_deposits()
