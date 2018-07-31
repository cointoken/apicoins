from flask import Flask,jsonify,make_response,request
from coins.btc import Btc
from coins.eth import Eth
from myjsonencoder import MyJSONEncoder
import datas

app = Flask(__name__)
app.json_encoder = MyJSONEncoder

def get_success_json(frist_key,thrid_key,content):
    datas.success_infos[frist_key]['data'][thrid_key] = content
    try:
        return jsonify(datas.success_infos[frist_key])
    except ValueError:
        print(' No JSON object could be decoded')


def init_coin(name):
    if datas.rpc_infos[name]['method']=='btc':
        btc = Btc(datas.rpc_infos[name]['rpc_port'],datas.rpc_infos[name]['rpc_user'],datas.rpc_infos[name]['rpc_password'])
        return btc
    elif datas.rpc_infos[name]['method']=='eth':
        eth = Eth(datas.rpc_infos[name]['rpc_port'])
        return eth


@app.route('/api/v1/getnewaddress/<name>')
def getnewaddress(name,methods=['GET']):
    if datas.rpc_infos[name]['method']=='btc':
        btc = init_coin(name)
        return get_success_json('new_address','address',btc.getnewaddress())
    elif datas.rpc_infos[name]['method']=='eth':
        eth = init_coin(name)
        return get_success_json('new_address','address',eth.getnewaddress())


@app.route('/api/v1/validateaddress/<name>/<address>')
def validateaddress(name,address):
    if datas.rpc_infos[name]['method']=='btc':
        btc = init_coin(name)
        return get_success_json('validate_address','info',btc.validateaddress(address))
    elif datas.rpc_infos[name]['method']=='eth':
        eth = init_coin(name)
        return get_success_json('validate_address','info',eth.validateaddress(address)) 


@app.route('/api/v1/getaccount/<name>/<address>')
def getaccount(name,address):
    if datas.rpc_infos[name]['method']=='btc':
        btc = init_coin(name)
        return get_success_json('account','info',btc.getaccount(address))


@app.route('/api/v1/listtransactions/<name>')
def listtransactions(name):
    if datas.rpc_infos[name]['method']=='btc':
        btc = init_coin(name)
        return get_success_json('transactions','info',btc.listtransactions('',20,0))


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
    app.run(host='0.0.0.0',port='8888')

