#from eth_rpc_client import Client # ethereum-rpc-client
from web3 import Web3, HTTPProvider
from sqlalchemy import create_engine
from datetime import datetime
import re
from .passphrase import Passphrase
from dbs.crud import CRUD
from dbs.models import Coins
import config
import requests
import json
import redis

class Eth(object):
    def __init__(self,rpc_port,name):
        #self.rpc_ip = '127.0.0.1'
        #self.rpc_port = rpc_port
        #self.rpc_eth = Client(self.rpc_ip,self.rpc_port)
        #self.passphrase = 'tow ciep iqppem dkpoq qoeook kapqoe'
        self.w3 = Web3(HTTPProvider('http://127.0.0.1:{0}'.format(rpc_port), request_kwargs={'timeout': 60}))
        self.name = name
        self.engine = create_engine(config.SQLALCHEMY_DATABASE_URI)


    def getnewaddress(self):
        # passphrase = Passphrase.generate(8)
        # coins = Coins(self.name,'',passphrase,datetime.now())
        # #engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
        # crud = CRUD(self.engine)
        # crud.coins_insert(coins)
 
        # address =''
        # try:
        #     address = self.w3.personal.newAccount(passphrase)
        # except:
        #     address =''
        # crud.coins_update(passphrase,address)
        # crud.close()
        # return address
        rs = redis.Redis(host='127.0.0.1',port=6379)
        rs_len = rs.llen('ethereum')
        address = ''
        if rs_len>1:
            address = bytes.decode(rs.lpop('ethereum'))
            #return bytes.decode(rs.lpop('ethereum'))
        return address

        #return self.w3.personal.importRawKey(private_key,self.passphrase)
    	#return self.rpc_eth.get_coinbase()
        #return self.w3.coinbase


    def validateaddress(self,adddress):
        reobj = re.match('^0x[a-fA-F0-9]{40}',adddress)
        return {"valid_address": True} if reobj else {"valid_address": False}
        #return  {"valid_address":self.w3.isAddress(adddress)}


    def sendTransaction(self,from_,to,amount):
        crud = CRUD(self.engine)
        passphrase = str(crud.coins_query_from_address(from_))
        crud.close()
        if passphrase and from_ and to:
            # flag = self.w3.personal.unlockAccount(from_, passphrase)
            # print(flag,passphrase)
            #  if flag:
            tx = { 'from': from_,'to': to,'value':self.w3.toWei(amount,'ether')}
            try:
                txid = self.w3.personal.sendTransaction(tx, 'stopwatch mascot sectional mounted finer neurosis malformed twerp')
                return txid
            except:
                return 'error'


    def test(self,address):
        if address:
            crud = CRUD(self.engine)
            passphrase = str(crud.coins_query_from_address(address))
            crud.close()
            if passphrase:
                flag = self.w3.personal.unlockAccount(address, passphrase)
                if flag:
                    return 'True'
                else:
                    return "False"


    @staticmethod
    def eth_get_transaction(address):
        #return self.w3.eth.getTransaction(transaction_hash)
        if address:
            eth_url = 'http://api.ethplorer.io/getAddressTransactions/{0}'.format(address)
            params = {'apiKey':'freekey'}
            r = requests.get(eth_url,params=params)
            rc = r.content
            if rc :
                js = json.loads(rc)
                try:
                    category = 'send' if js[0]['to']==address else 'receive'
                except:
                    return 'transactions_api_key_error'
                return {'address':address,'category':category,'time':js[0]['timestamp'],'txid':js[0]['hash'],'amount':str(js[0]['value'])}
        return 'transactions_error'

    
    @staticmethod
    def etc_get_transaction(address):
        if address:
            etc_url = 'https://api.gastracker.io/v1/addr/{0}/operations'.format(address)
            r = requests.get(etc_url)
            js = json.loads(r.content)
            if js:
                item = ''
                try:
                    item = js['items'][0]
                    category = 'send' if item['to']==address else 'receive'
                except:
                    return 'transactions_error'
            return {'address':address,'category':category,'time':item['timestamp'],'txid':item['hash'],'amount':str(item['value']['ether'])}
        return 'transactions_error'
            

    @staticmethod
    def eth_get_transactions(address,amount):
        result = 'transactions_empty'
        if address and amount>0:
            eth_url = 'http://api.ethplorer.io/getAddressTransactions/{0}'.format(address)
            params = {'apiKey':'freekey'}
            r = requests.get(eth_url,params=params)
            rc = r.content
            if rc :
                js = json.loads(rc)
                try:
                    if js:
                        #now_seconds = Coins.get_curr_seconds() 
                        for j in js: #now_seconds-j['timestamp']<1800 and
                            if  j['to']==address.lower() and j['value']==amount and j['success']==True:
                                return {'txid': j['hash']}
                except:
                    result = 'transactions_get_error'
        return result


    @staticmethod
    def etc_get_transactions(address,amount):
        result = 'transactions_empty'
        if address and amount>0:
            etc_url = 'https://api.gastracker.io/v1/addr/{0}/operations'.format(address)
            r = requests.get(etc_url)
            js = json.loads(r.content)
            if js:
                try:
                    js = js['items']
                    now_date = datetime.today().strftime('%Y-%m-%d')
                    for j in js:
                       if j['timestamp'].find(now_date)!=-1 and j['to']==address and j['value']['ether']==amount and j['isSend']==False and j['failed']==False:
                           return {'txid': j['hash']}
                except:
                    result = 'transactions_get_error'
        return result      

            
