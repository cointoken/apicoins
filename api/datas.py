
# -*- coding:utf-8 -*-

error_infos = {
    'not_found':{'status':404,'message':'not found','data':''},
    'forbidden':{'status':403,'message':'forbidden','data':''},
    'gateway_timeout':{'status':504,'message':'gateway timeout','data':''},
    'internal_server_error':{'status':500,'message':'internal server error','data':''}
}

status_code = {
	'404': 404,
	'400': 400,
    '403': 403,
	'405': 405,
	'500': 500,
	'504': 504
}

error_type = {'users_errors':{'interface_name':'','type':'user_error','details':''},
              'network_errors':{'interface_name':'','type':'network_error','details':''}}

users_errors = {'not_the_coin':'无此币，请对接存在的币'}

network_errors = {'ConnectionError':'区块服务器无法连接',
                  'JSONDecodeError':'无法获取区块数据或区块数据正在同步中'}

interface_name = {
	'newaddress':'getnewaddress',
	'valiaddress':'validateaddress',
	'transtatus':'gettranstatus'
}

rpc_infos = {
	'btc':{'rpc_port':8332,'rpc_user':'apx','rpc_password':'DEOXMEIO943JKDJFIE3312DFKIEOK','method':'btc'},
	'usdt':{'rpc_port':8338,'rpc_user':'usdt','rpc_password':'DJKQIEOOKDKLAKQOOEXMXMLLWOO','method':'btc'},
	'bch':{'rpc_port':8336,'rpc_user':'bch','rpc_password':'FEOPQSUOEODKLJAKLIEQPLALMNMXKIOQ','method':'btc'},
	'ltc':{'rpc_port':9337,'rpc_user':'exmoney','rpc_password':'TEIXMLW34803EDDKDLWQPAPW18389DKWOOPEOP','method':'btc'},
	'eth':{'rpc_port':8545,'method':'eth'},
	'etc':{'rpc_port':8546,'method':'eth'}
}

success_infos = {
    'new_address':{'status': 200,'message': 'success','data': { 'address': '' }},
	'validate_address':{'status': 200,'message': 'success','data': { 'info': '' }},
	'account':{'status': 200,'message': 'success','data': { 'info': '' }},
	'transactions':{'status': 200,'message': 'success','data': { 'info': '' }},
	'sendtoaddress':{'status': 200,'message': 'success','data': { 'info': '' }},
}