from eth_rpc_client import Client


class Eth(object):
	def __init__(self,rpc_port):
		self.rpc_ip = '127.0.0.1'
		self.rpc_port = rpc_port
        self.rpc_eth = Client(self.rpc_ip,self.rpc_port)


    def getnewaddress(self):
    	return self.rpc_eth.get_coinbase()

