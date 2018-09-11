from tasks import worker,create_engine,datetime
from coins.btc import Btc
from coins.eth import Eth
sys.path.append('..')
from dbs.models import  Deposits
from dbs.crud import CRUD
import config


@worker.task
def autotransfer():
    btc = Btc(8332,'apx','DEOXMEIO943JKDJFIE3312DFKIEOK')
    btc_accounts = btc.listaccounts()
    for key,value in btc_accounts.items():
        amount = btc_accounts[key] 
        try:
            amount = amount - amount*0.0005
            if amount >= 0.1 and amount <= 1 : #hot wallet
                txid = btc.sendfrom(key,"3FyyccCiTt3TUbvVXw3gsn6W5nRCUY1tPi",amount)
            elif amount>1: #cold walllet
                txid = btc.sendfrom(key,"1LAzU3gX58zBzKfbNXcyUZjhTeBVWJ7c1c",amount)
        except:
            pass

    ltc = Btc(8337,'exmoney','TEIXMLW34803EDDKDLWQPAPW18389DKWOOPEOP')
    ltc_accounts = ltc.listaccounts()
    for key,value in ltc_accounts.items():
        amount = ltc_accounts[key]
        try:
            if amount >=20:
                txid = ltc.sendfrom(key,"LXycyyLyE6VmdkJBtsZKPLqbZQWrRZTBu6",amount)
        except:
            pass

    usdt = Btc(8338,'usdt','DJKQIEOOKDKLAKQOOEXMXMLLWOO')
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    crud = CRUD(engine)
    usdt_datas = crud.deposits_query_from_currency('usdt')
    if len(usdt_datas)>0:
        for d in usdt_datas:
           txid = usdt.usdt_send_from(d['from_address'],'',d[amount])
           if txid!= 'none' or txid!='error':
               crud.deposits_update_from_deposit_id(d['deposit_id'],txid)

    eth = Eth(8545,'eth')
    eth_datas = crud.deposits_query_from_currency('eth')
    if len(eth_datas)>0:
        for d in eth_datas:
            txid = eth.sendTransaction(d['from_address'],'0xcF4eE0559801552b6d499CeC5a8775ca60242771',d[amount])
            if txid!= 'error':
                crud.deposits_update_from_deposit_id(d['deposit_id'],'',txid)
                
    etc = Eth(8546,'etc')
    etc_datas = crud.deposits_query_from_currency('etc')
    if len(etc_datas)>0:
        for d in etc_datas:
            txid = etc.sendTransaction(d['from_address'],'0xcae3775256dc09e1c7fda5d91ca0cac1b846595f',d[amount])
            if txid!= 'error':
                crud.deposits_update_from_deposit_id(d['deposit_id'],'',txid)

    crud.close()


            
    
    