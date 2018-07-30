from flask import Flask,jsonify,make_response,request
from coins.btc import Btc
from coins.eth import Eth
import datas

app = Flask(__name__)

def get_jsonaddress(address):
    datas.error_infos['success']['data']['address'] =  address
    return jsonify(datas.error_infos['success'])
    

def get_btc_address(rpc_port,rpc_user,rpc_pwd):
    btc = Btc(rpc_port,rpc_user,rpc_pwd)
    return get_jsonaddress(btc.getnewaddress())


def get_eth_address(rpc_port):
    eth = Eth(rpc_port)
    return get_jsonaddress(eth.getnewaddress())


@app.route('/api/v1/getnewaddress/<name>')
def getnewaddress(name,methods=['GET']):
    method = datas.rpc_infos.get(datas.rpc_infos[name]['method'],lambda:'not_found')
    return method(datas.rpc_infos[name]['rpc_port'],datas.rpc_infos[name]['rpc_user'],datas.rpc_infos[name]['rpc_password'])
    # if name=='btc':
    # 	btc = Btc(8332,'apx','DEOXMEIO943JKDJFIE3312DFKIEOK')
    #     return get_jsonaddress(btc.getnewaddress())
    # elif name=='bch':
    #     bch = Btc(8336,'bch','FEOPQSUOEODKLJAKLIEQPLALMNMXKIOQ')
    #     return get_jsonaddress(bch.getnewaddress())
    # elif name=='usdt':
    #     usdt = Btc(8338,'usdt','DJKQIEOOKDKLAKQOOEXMXMLLWOO')
    #     return get_jsonaddress(usdt.getnewaddress())
    # elif name=='ltc':
    #     ltc = Btc(9337,'exmoney','TEIXMLW34803EDDKDLWQPAPW18389DKWOOPEOP')
    #     return get_jsonaddress(ltc.getnewaddress())
    # elif name=='eth':
    #     eth = Eth(8545)
    #     return get_jsonaddress(eth.getnewaddress())
    # elif name=='etc':
    #     etc = Eth(8546)
    #     return get_jsonaddress(etc.getnewaddress())


@app.route('/api/v1/validateaddress/<name>/<address>')
def validateaddress(name,address):
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
    app.run(host='0.0.0.0',port='8080')

