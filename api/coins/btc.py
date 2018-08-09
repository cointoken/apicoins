#from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from .rpc import Proxy
from . import exc

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
