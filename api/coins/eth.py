from eth_rpc_client import Client # ethereum-rpc-client
import re


class Eth(object):
    def __init__(self,rpc_port):
        self.rpc_ip = '127.0.0.1'
        self.rpc_port = rpc_port
        self.rpc_eth = Client(self.rpc_ip,self.rpc_port)


    def getnewaddress(self):
    	return self.rpc_eth.get_coinbase()
    

    def validateaddress(self,adddress):
        reobj = re.match('^0x[a-fA-F0-9]{40}',adddress)
        return {"valid_address": True} if reobj else {"valid_address": False}
    

    def get_transaction_by_hash(self,txn_hash):
        return self.rpc_eth.get_transaction_by_hash(txn_hash)