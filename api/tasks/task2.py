from coins.eth import Eth
import redis
from tasks import worker,create_engine
from coins.passphrase import Passphrase
from dbs.crud import CRUD
from dbs.models import Coins
import config
from datetime import datetime


@worker.task
def get_ethereum_addresses():
    rs = redis.Redis(host='127.0.0.1',port=6379)
    re_len = rs.llen("ethereum")
    if re_len<30:
        engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
        crud = CRUD(engine)
        eth = Eth(8545,'eth')
        for i in range(0,10):
            passphrase = Passphrase.generate(8)
            coins = Coins('eth','',passphrase,datetime.now())
            crud.coins_insert(coins)
            address =''
            try:
                address = eth.w3.personal.newAccount(passphrase)
                if address:
                    crud.coins_update(passphrase,address)
                    rs.rpush("ethereum",address)
            except:
                address =''

        crud.close()

            