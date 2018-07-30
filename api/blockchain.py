from flask import Flask,jsonify
from flask.
from btc import Btc

app = Flask(__name__)

@app.route('/api/v1/getnewaddress/<name>')
def getnewaddress(name,methods=['GET']):
    if name=='btc':
        print('btc')
    	btc = Btc(8332,'apx','DEOXMEIO943JKDJFIE3312DFKIEOK')
    	return jsonify({'status': 200, 'message': 'success', 'data': { 'address': btc.getnewaddress()}})
    elif name=='bch':
        print('other')
    elif name=='usdt':
        usdt = Btc(8338,'usdt','DJKQIEOOKDKLAKQOOEXMXMLLWOO')
        return jsonify({'status': 200, 'message': 'success', 'data': { 'address': usdt.getnewaddress()}})
    elif name=='eth':
        pass
    elif name=='etc':
        pass


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')

