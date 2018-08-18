# -*- coding:utf-8 -*-
from flask import Flask,jsonify,make_response,request
import time
import logging
import logging.config
from coins.btc import Btc
from coins.eth import Eth
from myjsonencoder import MyJSONEncoder
import datas
import config


app = Flask(__name__)
app.json_encoder = MyJSONEncoder  

logging.config.dictConfig(config.LOGGING_CONFIG)
logger = logging.getLogger('default')

instances = {'btc': None,
            'ltc': None,
            'usdt': None,
            'bch': None,
            'eth': None,
            'etc': None}

objects =  {'btc': Btc(datas.rpc_infos['btc']['rpc_port'],datas.rpc_infos['btc']['rpc_user'],datas.rpc_infos['btc']['rpc_password']),
            'ltc': Btc(datas.rpc_infos['ltc']['rpc_port'],datas.rpc_infos['ltc']['rpc_user'],datas.rpc_infos['ltc']['rpc_password']),
            'usdt': Btc(datas.rpc_infos['usdt']['rpc_port'],datas.rpc_infos['usdt']['rpc_user'],datas.rpc_infos['usdt']['rpc_password']),
            'bch': Btc(datas.rpc_infos['bch']['rpc_port'],datas.rpc_infos['bch']['rpc_user'],datas.rpc_infos['bch']['rpc_password']),
            'eth': Eth(datas.rpc_infos['eth']['rpc_port'],'eth'),
            'etc': Eth(datas.rpc_infos['etc']['rpc_port'],'etc')
}

def get_curr_seconds():
    return int(round(time.time()))


def get_success_json(frist_key,third_key,content):
    datas.success_infos[frist_key]['data'][third_key] = content
    try:
        return jsonify(datas.success_infos[frist_key])
    except(TypeError,ValueError) as e:
        logger.error(e)


def get_errors_json(frist_key,content,status_code):
    datas.error_infos[frist_key]['data'] = content
    try:
        return make_response(jsonify(datas.error_infos[frist_key]),status_code)
    except(TypeError,ValueError) as e:
        logger.error(e)


def not_found_json(name):
    datas.error_type['users_errors']['interface_name'] = datas.interface_name[name]
    datas.error_type['users_errors']['details'] = datas.users_errors['not_the_coin']
    return get_errors_json('not_found',datas.error_type['users_errors'],datas.status_code['404'])   


@app.route('/api/v1/getnewaddress/<string:name>')
def getnewaddress(name,methods=['GET']):
    if name not in instances:
        return not_found_json('newaddress')
    try:
        instances[name] = objects[name]
    except Exception as e:
        logger.error('getnewaddress:{}'.format(e))
        instances[name] = objects[name]

    address = instances[name].getnewaddress()
    if name == 'ltc':
        address = Btc.ltc_get_address(address)
    #if name == 'bch':
    #   address = address[12:]  
    return get_success_json('new_address','address',address)


@app.route('/api/v1/validateaddress/<string:name>/<string:address>')
def validateaddress(name,address):
    if name not in instances:
        return not_found_json('valiaddress')

    try:
        instances[name] = objects[name]
    except Exception as e:
        logger.error('validateaddress:{}'.format(e))
        instances[name] = objects[name]

    validate = instances[name].validateaddress(address)
    if datas.rpc_infos[name]['method'] == 'btc':
        validate = {"valid_address": True} if validate['isvalid'] else {"valid_address": False}
    return get_success_json('validate_address','info',validate)

# @app.route('/api/v1/sendtoaddress/<string:name>/<string:address>/<int:amount>')
# def sendtoaddress(name,address,amount):
#     if  datas.rpc_infos[name]['method']=='btc':
#         return get_success_json('sendtoaddress','info',instances[name].sendtoaddress(address,amount))
#     #else：
#     #    pass

# @app.route('/api/v1/dumpprivkey/<string:name>/<string:address>')
# def dumpprivkey(name,address):
#     if name not in instances:
#         return not_found_json('valiaddress')

#     try:
#         instances[name] = objects[name]
#     except Exception as e:
#         logger.error('validateaddress:{}'.format(e))
#         instances[name] = objects[name]
#     key = instances[name].dumpprivkey(address)
#     return get_success_json('dumpprivkey','info',key)


@app.route('/api/v1/gettranstatus/<string:name>/<string:address>')
def listtransactions(name,address):
    if name not in instances:
        return not_found_json('transtatus')

    trans = []
    try:
        instances[name] = objects[name]
    except Exception as e:
        logger.error('gettranstatus:{}'.format(e))
        instances[name] = objects[name]
    if datas.rpc_infos[name]['method']=='btc':
        if name=='usdt':
            trans = instances[name] .usdt_get_trans(address)
            if not trans:
                trans =  Btc.usdt_get_deposit(address)
        else:
            result = instances[name].listtransactions('*',8000,0)
            for r in result:
                if r['address'] == address: #and (get_curr_seconds()-r['time'])<1200:
                    trans.append({'address':address,'category':r['category'],'time':r['time'],'txid':r['txid'],'amount':r['amount']})
        return get_success_json('transactions','info',trans)
    else:
        result = Eth.getTransaction(address)
        return get_success_json('transactions','info',result)


@app.errorhandler(403)
def forbidden(error):
    logger.error(repr(error))
    return make_response(jsonify(datas.error_infos['forbidden']),datas.status_code['403'])


@app.errorhandler(404)
def not_found(error):
    logger.error(repr(error))
    datas.error_type['users_errors']['interface_name'] = ''
    datas.error_type['users_errors']['details'] = datas.users_errors['not_the_interface']
    return get_errors_json('not_found',datas.error_type['users_errors'],datas.status_code['404']) 


@app.errorhandler(500)
def internal_server_error(error):
    error = repr(error)
    logger.error('500'+error)
    error = error[:error.find('(')]
    if error.find("\"")>=0:
        error = error[error.find("\"")+1:]

    datas.error_type['network_errors']['details'] = datas.network_errors[error]
    return get_errors_json('internal_server_error',datas.error_type['network_errors'],datas.status_code['500'])


@app.errorhandler(504)
def gateway_timeout(error):
    logger.error(repr(error))
    return make_response(jsonify(datas.error_infos['gateway_timeout']),datas.status_code['504'])

    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080',debug=False)

