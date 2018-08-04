# -*- coding:utf-8 -*-
from flask import Flask,jsonify,make_response,request
from coins.btc import Btc
from coins.eth import Eth
from myjsonencoder import MyJSONEncoder
import datas
import time
import sys
import requests
import urllib3


app = Flask(__name__)
app.json_encoder = MyJSONEncoder
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
            'eth': Eth(datas.rpc_infos['eth']['rpc_port']),
            'etc': Eth(datas.rpc_infos['etc']['rpc_port'])
}

def init_coins():
    for key,value in instances.items():
        instances[key] = objects[key]

def get_curr_seconds():
    return int(round(time.time()))


def get_success_json(frist_key,third_key,content):
    datas.success_infos[frist_key]['data'][third_key] = content
    try:
        return jsonify(datas.success_infos[frist_key])
    except(TypeError,ValueError) as e:
        print(e)


def get_errors_json(frist_key,content,status_code):
    datas.error_infos[frist_key]['data'] = content
    try:
        return make_response(jsonify(datas.error_infos[frist_key]),status_code)
    except(TypeError,ValueError) as e:
        print(e)


@app.route('/api/v1/getnewaddress/<string:name>')
def getnewaddress(name,methods=['GET']):
    if name not in instances:
        datas.error_type['users_errors']['interface_name'] = datas.interface_name['newaddress']
        datas.error_type['users_errors']['details'] = datas.users_errors['1000']
        return get_errors_json('not_found',datas.error_type['users_errors'],datas.status_code['404'])

    instances[name] = objects[name]
    address = instances[name].getnewaddress()
    if name == 'bch':
        address = address[12:]  
    return get_success_json('new_address','address',address)


@app.route('/api/v1/validateaddress/<string:name>/<string:address>')
def validateaddress(name,address):
    if name not in instances:
        datas.error_type['users_errors']['interface_name'] = datas.interface_name['valiaddress']
        datas.error_type['users_errors']['details'] = datas.users_errors['1000']
        return get_errors_json('not_found',datas.error_type['users_errors'],datas.status_code['404'])
     
    instances[name] = objects[name]
    validate = instances[name].validateaddress(address)

    return get_success_json('validate_address','info',validate)


@app.route('/api/v1/sendtoaddress/<string:name>/<string:address>/<int:amount>')
def sendtoaddress(name,address,amount):
    if  datas.rpc_infos[name]['method']=='btc':
        return get_success_json('sendtoaddress','info',instances[name].sendtoaddress(address,amount))
    #else：
    #    pass


@app.route('/api/v1/gettranstatus/<string:name>/<string:address>')
def listtransactions(name,address):
    if name not in instances:
        datas.error_type['users_errors']['interface_name'] = datas.interface_name['transtatus']
        datas.error_type['users_errors']['details'] = datas.users_errors['1000']
        return get_errors_json('not_found',datas.error_type['users_errors'],datas.status_code['404'])

    trans = []
    if datas.rpc_infos[name]['method']=='btc':
        instances[name] = objects[name]
        result = instances[name].listtransactions('*',8000,0)
        for r in result:
            if r['address'] == address: #and (get_curr_seconds()-r['time'])<1200:
                trans.append({'category':r['category'],'time':r['time'],'txid':r['txid'],'amount':r['amount']})
        return get_success_json('transactions','info',trans)
    else:
        pass


@app.errorhandler(403)
def forbidden(error):
    return make_response(jsonify(datas.error_infos['forbidden']),datas.status_code['403'])


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify(datas.error_infos['not_found']),datas.status_code['404'])


@app.errorhandler(Exception)
def internal_server_error(error):
    error = repr(error)
    error = error[:error.find('(')]
    if error.find("\"")>=0:
        error = error[error.find("\"")+1:]

    datas.error_type['network_errors']['details'] = datas.network_errors[error]
    return get_errors_json('internal_server_error',datas.error_type['network_errors'],datas.status_code['500'])


@app.errorhandler(504)
def gateway_timeout(error):
    return make_response(jsonify(datas.error_infos['gateway_timeout']),datas.status_code['504'])

    
if __name__ == "__main__":
    init_coins()
    app.run(host='0.0.0.0',port='8080',debug=False)

