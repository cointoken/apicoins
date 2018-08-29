#-*- coding: utf-8 -*-
#from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from .rpc import Proxy
from . import exc
import requests
import json
from datetime import datetime
import time


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
        if  bitcoinaddress and amount>0:
            txid = self.rpc_connection.sendtoaddress(bitcoinaddress,amount)
            if txid:
                return {'fromaddress':'','toaddress':bitcoinaddress,'category':'send','time':datetime.now(),'txid':txid,'amount':amount}


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
                    return {'address':address,'category':t['type'],'time':t['blocktime'],'txid':t['txid'],'amount':str(t['amount'])}
            except:
                return 'transactions_error'
        return 'transactions_error'


    def usdt_send_from(self,from_,to,amount):
        pass
        if from_ and to:
            balance = self.rpc_connection.omni_getallbalancesforaddress(from_)[0]['balance']
            if float(amount)<= float(balance):
                propertyid = 31
                txid = self.rpc_connection.omni_send(from_,to,propertyid,amount)
                if txid:
                    return {'fromaddress':from_,'toaddress':to,'category':'send','time':datetime.now(),'txid':txid,'amount':amount}
            return {"error":"提现数量大于可用数量"}


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


 

    ####给云平台提供交易查询使用
    @staticmethod
    def get_curr_seconds():
        return int(time.mktime(datetime.now().timetuple()))


    @staticmethod
    def btc_transactions(address,amount):
        result = 'transactions_empty'
        if address and amount >0:
            btc_url = 'https://bitaps.com/api/address/transactions/{0}'.format(address)
            try:
                r = requests.get(btc_url)
                if r.content:
                    js = json.loads(r.content)
                    if js:
                        amount = amount * 100000000
                        #now_seconds = Btc.get_curr_seconds()
                        for j in js:
                            if j[3]=='received' and j[4]=='confirmed' and j[7]==amount:
                                return {'txid':j[1]}
            except:
                result = 'transactions_get_error'
        return result


    @staticmethod
    def usdt_get_transactions(address,amount):
        result = 'transactions_empty'
        deposit_url = 'https://api.omniexplorer.info/v1/transaction/address'
        post_data = {
            'addr': address,
            'page': 0
        }
        if address:
            r = requests.post(deposit_url,data=post_data)
            j = json.loads(r.content)
            try:
                toaddress = j['address']
                ts = j['transactions']
                if ts:
                    #ow_seconds = Coins.get_curr_seconds() 
                    for t in ts: #and now_seconds-t['blocktime']<1800 
                        if toaddress == address and t['amount']==amount and t['valid']==True:
                            return {'txid': t['txid']}
            except:
                result = 'transactions_get_error'
        return result

    
    @staticmethod
    def ltc_get_transactions(address,amount):
        result = 'transactions_empty'
        ltc_url = 'https://chain.so/api/v2/address/ltc/{0}'
        if address:
            r = requests.get(ltc_url.format(address))
            j = json.loads(r.content)
            try:
                txs =  j['data']['txs']
                for tx in txs:
                    if 'incoming' in tx:
                        if float(tx['incoming']['value'])==amount and  tx['confirmations']>0:
                            return {'txid': tx['txid']}   
            except:
                result = 'transactions_get_error'
        return result

# unlock wallet
# sendtoaddress sendmany
##sendfrom  
# utxo 

    

