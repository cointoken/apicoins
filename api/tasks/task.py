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
        if amount >= 1:
            txid = btc.sendfrom(key,"",amount)

    ltc = Btc(8337,'exmoney','TEIXMLW34803EDDKDLWQPAPW18389DKWOOPEOP')
    ltc_accounts = ltc.listaccounts()
    for key,value in ltc_accounts.items():
        amount = ltc_accounts[key]
        if amount >=20:
            txid = ltc.sendfrom(key,"",amount)

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
            txid = eth.sendTransaction(d['from_address'],'',d[amount])
            if txid!= 'error':
                crud.deposits_update_from_deposit_id(d['deposit_id'],'',txid)
                
    etc = Eth(8546,'etc')
    etc_datas = crud.deposits_query_from_currency('etc')
    if len(etc_datas)>0:
        for d in etc_datas:
            txid = etc.sendTransaction(d['from_address'],'',d[amount])
            if txid!= 'error':
                crud.deposits_update_from_deposit_id(d['deposit_id'],'',txid)

    crud.close()


            
    
    