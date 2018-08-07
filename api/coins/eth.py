#from eth_rpc_client import Client # ethereum-rpc-client
from web3 import Web3, HTTPProvider
from sqlalchemy import create_engine
from datetime import datetime
import re
from passphrase import Passphrase
from dbs.crud import CRUD
from dbs.models import Coins
import config

class Eth(object):
    def __init__(self,rpc_port,name):
        #self.rpc_ip = '127.0.0.1'
        #self.rpc_port = rpc_port
        #self.rpc_eth = Client(self.rpc_ip,self.rpc_port)
        self.passphrase = 'tow ciep iqppem dkpoq qoeook kapqoe'
        self.w3 = Web3(HTTPProvider('http://127.0.0.1:{0}'.format(rpc_port), request_kwargs={'timeout': 60}))
        self.name = name


    def getnewaddress(self):
        passphrase = Passphrase.generate(8)
        coins = Coins(self.name,'',passphrase,datetime.now())
        engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
        crud = CRUD(engine)
        crud.insert(coins)

        address = self.w3.personal.newAccount(passphrase)
        crud.update(passphrase,address)
        crud.close()
        return address
        
        #return self.w3.personal.importRawKey(private_key,self.passphrase)
    	#return self.rpc_eth.get_coinbase()
        #return self.w3.coinbase


    def validateaddress(self,adddress):
        #reobj = re.match('^0x[a-fA-F0-9]{40}',adddress)
        #return {"valid_address": True} if reobj else {"valid_address": False}
        return  {"valid_address":self.w3.isAddress(adddress)}


    def sendTransaction(self,to,from_,value):
        return self.w3.eth.sendTransaction(to,from_,value)
       #return self.w3.eth.getBalance(address)
    
    def getTransaction(self,transaction_hash):
        return self.w3.eth.getTransaction(transaction_hash)
