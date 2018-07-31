from flask import Flask,jsonify,make_response,request
from coins.btc import Btc
from coins.eth import Eth
import datas

app = Flask(__name__)

def get_newaddress_json(address):
    datas.success_infos['new_address']['data']['address'] =  address
    return jsonify(datas.success_infos['new_address'])
    

def get_validateaddress_json(info):
    datas.success_infos['validate_address']['data']['info'] =  info
    return jsonify(datas.success_infos['validate_address'])
    

def init_coin(name):
    if name=='btc':
        btc = Btc(datas.rpc_infos[name]['rpc_port'],datas.rpc_infos[name]['rpc_user'],datas.rpc_infos[name]['rpc_password'])
        return btc
    elif name=='eth':
        eth = Eth(datas.rpc_infos[name]['rpc_port'])
        return eth


@app.route('/api/v1/getnewaddress/<name>')
def getnewaddress(name,methods=['GET']):
    if datas.rpc_infos[name]['method']=='btc':
        btc = init_coin(name)
        return get_newaddress_json(btc.getnewaddress())
    elif datas.rpc_infos[name]['method']=='eth':
        eth = init_coin(name)
        return get_newaddress_json(eth.getnewaddress())


@app.route('/api/v1/validateaddress/<name>/<address>')
def validateaddress(name,address):
    if datas.rpc_infos[name]['method']=='btc':
        btc = init_coin(name)
        return get_validateaddress_json(btc.validateaddress(address))


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

