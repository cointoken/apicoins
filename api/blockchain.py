# -*- coding:utf-8 -*-
from flask import Flask,jsonify,make_response,request
from coins.btc import Btc
from coins.eth import Eth
from myjsonencoder import MyJSONEncoder
import datas
import util

app = Flask(__name__)
app.json_encoder = MyJSONEncoder
instances = {'btc':None,
            'ltc':None,
            'usdt':None,
            'bch':None,
            'eth':None,
            'etc':None}


def get_success_json(frist_key,thrid_key,content):
    datas.success_infos[frist_key]['data'][thrid_key] = content
    try:
        return jsonify(datas.success_infos[frist_key])
    except ValueError:
        print(' No JSON object could be decoded')


def init_coins():
    instances['btc'] = Btc(datas.rpc_infos['btc']['rpc_port'],datas.rpc_infos['btc']['rpc_user'],datas.rpc_infos['btc']['rpc_password'])
    instances['ltc'] = Btc(datas.rpc_infos['ltc']['rpc_port'],datas.rpc_infos['ltc']['rpc_user'],datas.rpc_infos['ltc']['rpc_password'])
    instances['usdt'] = Btc(datas.rpc_infos['usdt']['rpc_port'],datas.rpc_infos['usdt']['rpc_user'],datas.rpc_infos['usdt']['rpc_password'])
    instances['bch'] = Btc(datas.rpc_infos['bch']['rpc_port'],datas.rpc_infos['bch']['rpc_user'],datas.rpc_infos['bch']['rpc_password'])
    instances['eth'] = Eth(datas.rpc_infos['eth']['rpc_port'])
    instances['etc'] = Eth(datas.rpc_infos['etc']['rpc_port'])


@app.route('/api/v1/getnewaddress/<name>')
def getnewaddress(name,methods=['GET']):
    return get_success_json('new_address','address',instances[name].getnewaddress())


@app.route('/api/v1/validateaddress/<name>/<address>')
def validateaddress(name,address):
    return get_success_json('validate_address','info',instances[name].validateaddress(address))


@app.route('/api/v1/gettranstatus/<name/<address>')
def listtransactions(name,address):
    if datas.rpc_infos[name]['method']=='btc':
        result = instances[name].listtransactions('',1000,0)
        for r in result:
            if r['address'] == address:
                if  (Util.get_curr_seconds()-r['time'])<1200:
                    pass
        #return get_success_json('transactions','info',btc.listtransactions('',1000,0))

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
    app.run(host='0.0.0.0',port='8888')

