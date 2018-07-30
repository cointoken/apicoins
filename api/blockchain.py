from flask import Flask,jsonify,make_response,request
from btc import Btc
from eth import Eth

app = Flask(__name__)
address_data = {
    'status': 200,
    'message': 'success',
    'data': { 'address': '' }
}
not_found_data = {'status':404,'message':'not found','data':''}
forbidden_data =  {'status':403,'message':'forbidden','data':''}
gateway_timeout_data = {'status':504,'message':'gateway timeout','data':''}


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


@app.errorhandler(403)
def forbidden(error):
    return make_response(jsonify(not_found_data),403)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify(not_found_data),404)


@app.errorhandler(504)
def not_found(error):
    return make_response(jsonify(not_found_data),404)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')

