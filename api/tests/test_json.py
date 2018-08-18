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

if __name__ == '__main__':
    print(ltc_get_address('MJFUvSKPqC8FuEQixFsWNzB5Rs6a9GKjyJ'))