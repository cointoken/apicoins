from tasks import worker,create_engine,datetime
from celery.utils.log import get_task_logger
from coins.btc import Btc
from coins.eth import Eth
import sys
sys.path.append('..')
from dbs.models import  Deposits
from dbs.crud import CRUD
import config


log = get_task_logger(__name__)
@worker.task
def autotransfer():
    # btc = Btc(8332,'apx','DEOXMEIO943JKDJFIE3312DFKIEOK')
    # btc_accounts = btc.listaccounts()
    # amount = 0.0
    # for key,value in btc_accounts.items():
    #     amount = amount + btc_accounts[key]
    
    # try:
    #     amount = amount - amount*0.0001
    #     if amount >= 0.1 and amount <= 1 : #hot wallet
    #         txid = btc.sendfrom('payment',"3FyyccCiTt3TUbvVXw3gsn6W5nRCUY1tPi",amount)
    #     elif amount>1: #cold walllet
    #         txid = btc.sendfrom('payment',"1LAzU3gX58zBzKfbNXcyUZjhTeBVWJ7c1c",amount)
    # except Exception as e:
    #     log.error('bitcoin:'+repr(e))

    # ltc = Btc(8337,'exmoney','TEIXMLW34803EDDKDLWQPAPW18389DKWOOPEOP')
    # ltc_accounts = ltc.listaccounts()
    # for key,value in ltc_accounts.items():
    #     amount = ltc_accounts[key]
    #     try:
    #         if amount >=20:
    #             txid = ltc.sendfrom(key,"LXycyyLyE6VmdkJBtsZKPLqbZQWrRZTBu6",amount)
    #     except Exception as e:
    #         log.error('litecoin:'+repr(e))

    # usdt = Btc(8338,'usdt','DJKQIEOOKDKLAKQOOEXMXMLLWOO')
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    crud = CRUD(engine)
    # usdt_datas = crud.deposits_query_from_currency('usdt')
    # if len(usdt_datas)>0:
    #     for d in usdt_datas:
    #         try:
    #             txid = usdt.usdt_send_from(d.from_address,'',d.amount)
    #             if txid!= 'none' or txid!='error':
    #                 crud.deposits_update_from_deposit_id(d.deposit_id,txid)
    #         except Exception as e:
    #             log.error('usdt:'+repr(e))


    eth = Eth(8545,'eth')
    eth_datas = crud.deposits_query_from_currency('eth')
    eth_to_address = '0xcF4eE0559801552b6d499CeC5a8775ca60242771'
    if eth_datas:
        for d in eth_datas:
            try:
                cc_amount = eth.getBalance(d.from_address,'')
                if cc_amount>=d.amount:
                    result  = eth.sendTransaction(d.from_address,eth_to_address,d.amount)
                    if result[0]:
                        crud.deposits_update_from_deposit_id(d.deposit_id,'',result[1])
                    else:
                        log.error('ethereum:'+result[1])
            except Exception as e:
                log.error('ethereum:'+repr(e))

                
    etc = Eth(8546,'etc')
    etc_datas = crud.deposits_query_from_currency('etc')
    etc_to_address = '0xcae3775256dc09e1c7fda5d91ca0cac1b846595f'
    if etc_datas:
        for d in etc_datas:
            try:
                cc_amount = etc.getBalance(d.from_address,'')
                if cc_amount>=d.amount:
                    result = etc.sendTransaction(d.from_address,etc_to_address,d.amount)
                    if result[0]:
                        crud.deposits_update_from_deposit_id(d.deposit_id,'',result[1])
                    else:
                        log.error('ethereum cash:'+result[1])
            except Exception as e:
                log.error('ethereum cash:'+repr(e))

    crud.close()


            
    
    