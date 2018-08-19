import json
import requests
import collections


data = "{\"status\":200,\"message\":\"success\", \"data\":{\"deposits\":[{\"fund_uid\":\"\",\"amount\":10000,\"currency\":\"btc\"},{\"fund_uid\":\"\",\"amount\":8888,\"currency\":\"ltc\"}] }}"


def test_getdata():
    url = 'http://47.75.91.163:8080/api/v1/getnewaddress/ltc'
    r = requests.get(url)
    j = json.loads(r.content)
    if isinstance(j,str):
        print(j)
    elif isinstance(j,dict):
        print('dict')
    print(j['data'])
    dic = {}
    dic['cc'] = 'ccc'
    dic['dd'] = 'ddd'
    dic['ee'] = 'ee'
    for key,value in dic.items():
        print(dic[key])   
    
def test_data():
    j = json.loads(data)
    if isinstance(j,str):
        print('str')
    elif isinstance(j,dict):
        print('dict')
    arrs = j['data']['deposits']
    for a in arrs:
        print(a['currency'])

def test_str():
    s ={'category':'sdoio'}
    if not s:
        print('no')
    else:
        print('yes')

def ltc_get_address(address):
    if address:
        ltc_url =  'https://chain.so/api/v2/address/LTC/{0}'.format(address)
        r = requests.get(ltc_url)
        if r.content:
            j =  json.loads(r.content)
            return j['data']['address']
    return ''

def testdict(key):
    dic = ''
    dic={'1':1222,'2':1444}
    
    if dic[key]:
        print(dic[key])
    else:
        print('error')


def getTransaction(address):
        #return self.w3.eth.getTransaction(transaction_hash)
    if address:
        eth_url = 'http://api.ethplorer.io/getAddressTransactions/{0}'.format(address)
        params = {'apiKey':'freekey11'}
        r = requests.get(eth_url,params=params)
        rc = r.content
        if rc :
            js = json.loads(rc)
            try:
                category = 'send' if js[0]['to']==address else 'receive'
            except:
                return rc
        return {'address':address,'category':category,'time':js[0]['timestamp'],'txid':js[0]['hash'],'amount':js[0]['value']}
    return {"error":{"code":100,"message":'Invalid address'}}


def etc_get_transaction(address):
    if address:
        etc_url = 'https://api.gastracker.io/v1/addr/{0}/operations'.format(address)
        r = requests.get(etc_url)
        js = json.loads(r.content)
        if js:
            item = ''
            try:
                item = js['items'][0]
                category = 'send' if item['to']==address else 'receive'
            except:
                return 'transactions_api_key_error'
            return {'address':address,'category':category,'time':item['timestamp'],'txid':item['hash'],'amount':item['value']['ether']}
            

if __name__ == '__main__':
    #print(getTransaction(''))
    print(etc_get_transaction('0xCd6b6de6e4C471368108b895C899F7Bd0e48f305'))
    #testdict("{'234':123}")