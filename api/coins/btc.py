#from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from .rpc import Proxy
from . import exc
import requests
import json

class Btc(object):
    def __init__(self,rpc_port,rpc_user,rpc_password):
        self.rpc_ip = '127.0.0.1'
        self.rpc_user = rpc_user
        self.rpc_password = rpc_password
        self.rpc_port = rpc_port
        self.rpc_connection = Proxy("http://%s:%s@%s:%s"%(self.rpc_user,self.rpc_password,self.rpc_ip,self.rpc_port))


    def getnewaddress(self):
        return self.rpc_connection.getnewaddress("")
    
    
    def getaccount(self,bitcoinaddress):
        return self.rpc_connection.getaccount(bitcoinaddress)


    def listtransactions(self,account,count,from_):
    	return self.rpc_connection.listtransactions(account,count,from_)
    

    def validateaddress(self,bitcoinaddress):
    	return self.rpc_connection.validateaddress(bitcoinaddress)

    
    def sendtoaddress(self,bitcoinaddress,amount):
        return self.rpc_connection.sendtoaddress(bitcoinaddress,amount)


    def sendfrom(self,fromaccount,tobitcoinaddress,amount):
    	return self.rpc_connection.sendfrom(fromaccount,tobitcoinaddress,amount)
    
    
    '''
    从比特币地址生成私钥
    '''
    def dumpprivkey(self,address):
        return self.rpc_connection.dumpprivkey(address)


    
    @staticmethod
    def usdt_get_deposit(address):
        deposit_url = 'https://api.omniexplorer.info/v1/transaction/address'
        post_data = {
            'addr': address,
            'page': 0
        }
        r = requests.post(deposit_url,data=post_data)
        j = json.loads(r.content)
        ts = j['transactions']
        return {'category':ts[0]['type'],'time':ts[0]['blocktime'],'txid':ts[0]['txid'],'amount':ts[0]['amount']}

     
    def usdt_get_trans(self):
        ol = self.rpc_connection.omni_listtransactions()
        print(ol[0]['referenceaddress'])



if __name__ == '__main__':
    btc = Btc('usdt','DJKQIEOOKDKLAKQOOEXMXMLLWOO',8338)
    btc.usdt_get_trans()

    

