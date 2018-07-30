from flask import Flask,jsonify,make_response,request
from coins.btc import Btc
from coins.eth import Eth

app = Flask(__name__)
address_data = {
    'status': 200,
    'message': 'success',
    'data': { 'address': '' }
}
not_found_data = {'status':404,'message':'not found','data':''}
forbidden_data =  {'status':403,'message':'forbidden','data':''}
gateway_timeout_data = {'status':504,'message':'gateway timeout','data':''}
internal_server_error_data  = {'status':500,'message':'internal server error','data':''}

def get_jsonaddress(address):
    address_data['data']['address'] =  address
    return jsonify(address_data)
    

@app.route('/api/v1/getnewaddress/<name>')
def getnewaddress(name,methods=['GET']):
    if name=='btc':
    	btc = Btc(8332,'apx','DEOXMEIO943JKDJFIE3312DFKIEOK')
        return get_jsonaddress(btc.getnewaddress())
    elif name=='bch':
        bch = Btc(8336,'bch','FEOPQSUOEODKLJAKLIEQPLALMNMXKIOQ')
        return get_jsonaddress(bch.getnewaddress())
    elif name=='usdt':
        usdt = Btc(8338,'usdt','DJKQIEOOKDKLAKQOOEXMXMLLWOO')
        return get_jsonaddress(usdt.getnewaddress())
    elif name=='ltc':
        ltc = Btc(9337,'exmoney','TEIXMLW34803EDDKDLWQPAPW18389DKWOOPEOP')
        return get_jsonaddress(ltc.getnewaddress())
    elif name=='eth':
        eth = Eth(8545)
        return get_jsonaddress(eth.getnewaddress())
    elif name=='etc':
        etc = Eth(8546)
        return get_jsonaddress(etc.getnewaddress())


@app.route('/api/v1/validateaddress/<name>/<address>')
def validateaddress(name,address):
      



@app.errorhandler(403)
def forbidden(error):
    return make_response(jsonify(not_found_data),403)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify(not_found_data),404)


@app.errorhandler(500)
def internal_server_error(error):
    return make_response(jsonify(internal_server_error_data),500)


@app.errorhandler(504)
def gateway_timeout(error):
    return make_response(jsonify(gateway_timeout_data),504)





if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')

