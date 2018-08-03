# -*- coding:utf-8 -*-
from flask import Flask,jsonify,make_response,request
from coins.btc import Btc
from coins.eth import Eth
from myjsonencoder import MyJSONEncoder
import datas
import time

app = Flask(__name__)
app.json_encoder = MyJSONEncoder
instances = {'btc':None,
            'ltc':None,
            'usdt':None,
            'bch':None,
            'eth':None,
            'etc':None}


def init_coins():
    instances['btc'] = Btc(datas.rpc_infos['btc']['rpc_port'],datas.rpc_infos['btc']['rpc_user'],datas.rpc_infos['btc']['rpc_password'])
    instances['ltc'] = Btc(datas.rpc_infos['ltc']['rpc_port'],datas.rpc_infos['ltc']['rpc_user'],datas.rpc_infos['ltc']['rpc_password'])
    instances['usdt'] = Btc(datas.rpc_infos['usdt']['rpc_port'],datas.rpc_infos['usdt']['rpc_user'],datas.rpc_infos['usdt']['rpc_password'])
    instances['bch'] = Btc(datas.rpc_infos['bch']['rpc_port'],datas.rpc_infos['bch']['rpc_user'],datas.rpc_infos['bch']['rpc_password'])
    instances['eth'] = Eth(datas.rpc_infos['eth']['rpc_port'])
    instances['etc'] = Eth(datas.rpc_infos['etc']['rpc_port'])


def get_curr_seconds():
    return int(round(time.time()))


def get_success_json(frist_key,thrid_key,content):
    datas.success_infos[frist_key]['data'][thrid_key] = content
    try:
        return jsonify(datas.success_infos[frist_key])
    except ValueError:
        print(' No JSON object could be decoded')


@app.route('/api/v1/getnewaddress/<string:name>')
def getnewaddress(name,methods=['GET']):
    address = ''
    try:
        address = instances[name].getnewaddress()
    except e:
        print(e.message)
    finally:
        init_coins()
        address = instances[name].getnewaddress()
    if name == 'bch':
        address = address[12:]  
    return get_success_json('new_address','address',address)


@app.route('/api/v1/validateaddress/<string:name>/<string:address>')
def validateaddress(name,address):
    validate = ''
    try:
        validate = instances[name].validateaddress(address)
    except e:
        print(e.message)
    finally:
        init_coins()
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
    trans = []
    if datas.rpc_infos[name]['method']=='btc':
        result = ''
        try:
            result = instances[name].listtransactions('*',8000,0)
        except e:
            print(e.message)
        finally:
            init_coins()
            result = instances[name].listtransactions('*',8000,0)
        for r in result:
            if r['address'] == address: #and (get_curr_seconds()-r['time'])<1200:
                trans.append({'category':r['category'],'time':r['time'],'txid':r['txid'],'amount':r['amount']})
        return get_success_json('transactions','info',trans)
    else:
        pass

        
@app.errorhandler(403)
def forbidden(error):
    return make_response(jsonify(datas.error_infos['forbidden']),403)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify(datas.error_infos['not_found']),404)


@app.errorhandler(500)
def internal_server_error(error):
    return make_response(jsonify(datas.error_infos['internal_server_error']),500)


@app.errorhandler(504)
def gateway_timeout(error):
    return make_response(jsonify(datas.error_infos['gateway_timeout']),504)

    
if __name__ == "__main__":
    init_coins()
    app.run(host='0.0.0.0',port='8080')

