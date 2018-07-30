from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

class Btc(object):
    def __init__(self,rpc_port,rpc_user,rpc_password):
        self.rpc_ip = '127.0.0.1'
        self.rpc_user = rpc_user
        self.rpc_password = rpc_password
        self.rpc_port = rpc_port
	self.rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(self.rpc_user,self.rpc_password,self.rpc_ip,self.rpc_port))

    def getnewaddress(self):
        return self.rpc_connection.getnewaddress("")

