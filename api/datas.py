
error_infos = {
    'success':{'status': 200,'message': 'success','data': { 'address': '' }},
    'not_found':{'status':404,'message':'not found','data':''},
    'forbidden':{'status':403,'message':'forbidden','data':''},
    'gateway_timeout':{'status':504,'message':'gateway timeout','data':''},
    'internal_server_error':{'status':500,'message':'internal server error','data':''}
}

rpc_infos = {
	'btc':{'rpc_port':8332,'rpc_user':'apx','rpc_password':'DEOXMEIO943JKDJFIE3312DFKIEOK','method':'get_btc_address'},
	'usdt':{'rpc_port':8338,'rpc_user':'usdt','rpc_password':'DJKQIEOOKDKLAKQOOEXMXMLLWOO','method':'get_btc_address'},
	'bch':{'rpc_port':8336,'rpc_user':'bch','rpc_password':'FEOPQSUOEODKLJAKLIEQPLALMNMXKIOQ','method':'get_btc_address'},
	'ltc':{'rpc_port':9337,'rpc_user':'exmoney','rpc_password':'TEIXMLW34803EDDKDLWQPAPW18389DKWOOPEOP','method':'get_btc_address'},
	'eth':{'rpc_port':8545,'method':'get_eth_address'},
	'etc':{'rpc_port':8546,'method':'get_eth_address'}
}