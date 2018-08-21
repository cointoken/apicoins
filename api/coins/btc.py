#-*- coding: utf-8 -*-
#from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from .rpc import Proxy
from . import exc
import requests
import json
from datetime import datatime

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
        if  bitcoinaddress:
            txid = self.rpc_connection.sendtoaddress(bitcoinaddress,amount)
            if txid:
                return {'fromaddress':from_,'toaddress':to,'category':'send','time':datatime.now(),'txid':txid,'amount':amount}


    def sendfrom(self,fromaccount,tobitcoinaddress,amount):
        return self.rpc_connection.sendfrom(fromaccount,tobitcoinaddress,amount)
        # if  tobitcoinaddress:
        #     txid = self.rpc_connection.sendtoaddress(tobitcoinaddress,amount)
        #     if txid:
        #         return {'fromaddress':from_,'toaddress':to,'category':'send','time':datatime.now(),'txid':txid,'amount':amount}
    
    
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
        if address:
            r = requests.post(deposit_url,data=post_data)
            j = json.loads(r.content)
            try:
                ts = j['transactions']
                return {'address':address,'category':ts[0]['type'],'time':ts[0]['blocktime'],'txid':ts[0]['txid'],'amount':ts[0]['amount']}
            except:
                return 'transactions_error'
        return 'transactions_error'

     
    def usdt_get_trans(self,address):
        ts = self.rpc_connection.omni_listtransactions()
        for t in ts:
            try:
                if t['referenceaddress'] == address:
                    return {'address':address,'category':t['type'],'time':t['blocktime'],'txid':t['txid'],'amount':t['amount']}
            except:
                return 'transactions_error'
        return 'transactions_error'


    def usdt_send_from(self,from_,to,amount):
        pass
        # if from_ and to:
        #     balance = self.rpc_connection.omni_getallbalancesforaddress(from_)[0]['balance']
        #     if float(amount)<= float(balance):
        #         propertyid = 31
        #         txid = self.rpc_connection.omn​​i_send(from_,to,propertyid,amount)
        #         if txid:
        #             return {'fromaddress':from_,'toaddress':to,'category':'send','time':datatime.now(),'txid':txid,'amount':amount}
        #     return {"error":"提现数量大于可用数量"}


    def ltc_get_tranaddress(self,address):
        j = self.rpc_connection.validateaddress(address)
        if j:
            try:
                return j['address']
            except:
                return 'transactions_error'
        return 'transactions_error'             
    
    
    @staticmethod
    def ltc_get_address(address):
        if address:
            ltc_url =  'https://chain.so/api/v2/address/LTC/{0}'.format(address)
            r = requests.get(ltc_url)
            if r.content:
                j =  json.loads(r.content)
                try:
                    return j['data']['address']
                except:
                    return 'transactions_error'
        return 'transactions_error'


# if __name__=='__main__':
#     print(Btc.ltc_get_address('MJFUvSKPqC8FuEQixFsWNzB5Rs6a9GKjyJ'))

    

