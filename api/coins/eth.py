from eth_rpc_client import Client # ethereum-rpc-client
#from web3 import Web3, HTTPProvider
import re


class Eth(object):
    def __init__(self,rpc_port):
        self.rpc_ip = '127.0.0.1'
        self.rpc_port = rpc_port
        self.rpc_eth = Client(self.rpc_ip,self.rpc_port)
        #self.w3 = Web3(HTTPProvider('http://127.0.0.1:{0}'.format(rpc_port)))

    def getnewaddress(self):
    	return self.rpc_eth.get_coinbase()
        #return self.w3.eth.coinbase


    def validateaddress(self,adddress):
        reobj = re.match('^0x[a-fA-F0-9]{40}',adddress)
        return {"valid_address": True} if reobj else {"valid_address": False}
        #return  {"valid_address":self.w3.isAddress}


    def getbalance(self,address):
        pass
       #return self.w3.eth.getBalance(address)
